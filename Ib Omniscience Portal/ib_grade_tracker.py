import json
import os

# GLOBAL CONFIGURATION
script_dir = os.path.dirname(os.path.abspath(__file__))
IB_DATA_FILE = os.path.join(script_dir, 'ib_data.json')

# LAYER 1: DATA PERSISTENCE (JSON File Storage)
# =====================================================================
def load_ib_data_from_file():
    if not os.path.exists(IB_DATA_FILE): 
        return {}
    try:
        with open(IB_DATA_FILE, 'r') as file:
            parsed_data = json.load(file)
        return parsed_data
    
    except json.JSONDecodeError:
        return {}
    
def save_ib_data_to_file(ib_data):
    with open(IB_DATA_FILE, 'w') as file:
        json.dump(ib_data, file, indent=4)

# LAYER 2: LAB FUNCTIONS (CORE LOGIC RULES)
# =====================================================================
IB_BOUNDARIES = {
    7: (85, 100), 6: (70, 84.99), 5: (60, 69.99),
    4: (50, 59.99), 3: (40, 49.99), 2: (25, 39.99), 1: (0, 24.99)

}

def add_subject(ib_data, subject_name, level):
    subject_name = subject_name.title()
    level = level.upper().strip()

    if level not in ['HL', 'SL']:
        return f"Error: {level} is not a valid level. Use 'HL' or 'SL'!"
    
    if subject_name in ib_data:
        return f"Error: Subject '{subject_name}' already exists. Cannot add duplicates!"
    
    ib_data[subject_name] = {
        "level": level,
        "scores": [],
        "final_scale_grade": 1

    }

    save_ib_data_to_file(ib_data)

    return f"Subject '{subject_name}' added successfully with level {level}."

def update_core_points(ib_data, tok_grade, ee_grade):
    tok_grade = tok_grade.upper().strip()
    ee_grade = ee_grade.upper().strip()
    
    valid_grades = ['A', 'B', 'C', 'D', 'E']
    if tok_grade not in valid_grades or ee_grade not in valid_grades:
        return f"Error: Invalid grades entered. Use 'A', 'B', 'C', 'D', or 'E' only!"

    matrix = {
        ('A', 'A'): 3, ('A', 'B'): 3, ('A', 'C'): 2, ('A', 'D'): 2,
        ('B', 'A'): 3, ('B', 'B'): 2, ('B', 'C'): 2, ('B', 'D'): 1,
        ('C', 'A'): 2, ('C', 'B'): 2, ('C', 'C'): 1, ('C', 'D'): 0,
        ('D', 'A'): 2, ('D', 'B'): 1, ('D', 'C'): 0, ('D', 'D'): 0
    }

    # Matrix determines bonus 0-3; grades of E result in 0 points and failing condition
    bonus_points = matrix.get((tok_grade, ee_grade), 0)

    ib_data["core_bonus"] = {
        "tok": tok_grade,
        "ee": ee_grade,
        "points": bonus_points
    
    }

    save_ib_data_to_file(ib_data)
    msg = f"Success: TOK {tok_grade} and EE {ee_grade} updated. {bonus_points} Core points added."
    if tok_grade == 'E' or ee_grade == 'E':
        msg += " (Failing Condition: Grade E detected)"
    return msg

def log_raw_score(ib_data, subject_name, percentage_mark):
    subject_name = subject_name.title().strip()
    
    if subject_name not in ib_data:
        return f"Error: Subject '{subject_name}' is not registered yet!"
    
    try:
        mark = float(percentage_mark)
        if not (0 <= mark <= 100):
            return "Error: Mark must be a valid percentage between 0 and 100."
    except ValueError:
        return "Error: Percentage mark must be a numerical value."
        
    ib_data[subject_name]["scores"].append(mark)
    
    running_avg = sum(ib_data[subject_name]["scores"]) / len(ib_data[subject_name]["scores"])
    
    assigned_scale_grade = 1 
    for grade, boundaries in IB_BOUNDARIES.items():
        low_bound, high_bound = boundaries
        if low_bound <= running_avg <= high_bound:
            assigned_scale_grade = grade
            break 
            
    ib_data[subject_name]["final_scale_grade"] = assigned_scale_grade
    
    save_ib_data_to_file(ib_data)
    
    # Fixed: Matched the exact variable names used above
    return f"Score {mark}% logged for {subject_name}. New Avg: {running_avg:.2f}% -> Converted IB Grade: {assigned_scale_grade}"

def calculate_diploma_score(ib_data):
    hl_scores = []
    sl_scores = []
    total_subject_points = 0
    
    for subject, details in ib_data.items():
        if subject == "core_bonus":
            continue
            
        grade = details["final_scale_grade"]
        total_subject_points += grade
        
        if details["level"] == "HL":
            hl_scores.append(grade)
        elif details["level"] == "SL":
            sl_scores.append(grade)
        
    bonus_points = ib_data.get("core_bonus", {}).get("points", 0)
    final_score = total_subject_points + bonus_points

    passing_status = True
    reasons = []

    if final_score < 24:
        passing_status = False
        reasons.append(f"Total score ({final_score}) is less than the minimum points of 24.")

    # Rule: Grade of E in TOK or EE is a failing condition
    core = ib_data.get("core_bonus", {})
    if core.get("tok") == "E" or core.get("ee") == "E":
        passing_status = False
        reasons.append("An 'E' grade in TOK or EE results in an automatic failure.")
    
    # Requirement: If subjects >= 6, check specific level distributions
    num_subjects = len([s for s in ib_data if s != "core_bonus"])
    if num_subjects >= 6:
        sorted_hl = sorted(hl_scores, reverse=True)
        if sum(sorted_hl[:3]) < 12:
            passing_status = False
            reasons.append(f"Top 3 HL subjects total ({sum(sorted_hl[:3])}) is less than minimum points of 12.")
        
        if sum(sl_scores) < 9:
            passing_status = False
            reasons.append(f"SL subjects total ({sum(sl_scores)}) is less than minimum points of 9.")

    if 1 in hl_scores or 1 in sl_scores:
        passing_status = False
        reasons.append("A grade of 1 in any subject results in a failure.")
    
    report = f"\n====== IB Diploma Score Report ======\n"
    report += f"Total Subject Points: {total_subject_points}\n"
    report += f"TOK/EE Bonus Points: +{bonus_points}\n"
    report += f"Final Score: {final_score} / 45 \n"
    report += f"--------------------------------\n"

    if passing_status:
        report += "Congratulations! You are on track to earn your IB Diploma! 🎉\n"
    else:
        report += "Warning: You are currently not on track to earn your IB Diploma.\n"
        for reason in reasons:
            report += f"- {reason}\n"
    return report

# LAYER 3: TERMINAL INTERFACE (USER MENU LOOP)
# =====================================================================
def main():
    test_ib_profile = load_ib_data_from_file()

    if "core_bonus" not in test_ib_profile:
        test_ib_profile["core_bonus"] = {
            "tok": None,
            "ee": None,
            "points": 0
        }

    while True:
        print("\n=== IB Grade Tracker Menu ===")
        print("1. View DP Dashboard (Scores, Averages & Diploma Status)")
        print("2. Register a New DP Course (HL/SL)")
        print("3. Log a Raw Assignment Percentage Mark")
        print("4. Update TOK/EE Core Bonus Matrix")
        print("5. Remove a Course Record")
        print("6. Exit Tracker")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            if len(test_ib_profile) <= 1: 
                print("\n⚠️ No subjects registered yet. Please register a course first!")
            else:
                print("\n================ INDIVIDUAL SUBJECTS ================")
                for subject, details in test_ib_profile.items():
                    if subject == "core_bonus":
                        continue
                    
                    avg_text = "No scores logged yet."
                    if len(details["scores"]) > 0:
                        avg_text = f"{sum(details['scores']) / len(details['scores']):.2f}%"
                    
                    print(f" {subject} ({details['level']})")
                    print(f" Logged Scores: {details['scores']}")
                    print(f" Current Average: {avg_text}")
                    print(f" Current IB Grade: {details['final_scale_grade']}")
                    print("-" * 40)
                
                print(calculate_diploma_score(test_ib_profile))

        elif choice == '2':
            subject_name = input("Enter subject name: ").strip()
            level = ""
            while level not in ["HL", "SL"]:
                level = input("Enter subject level (HL/SL): ").strip().upper()
            
            response = add_subject(test_ib_profile, subject_name, level)
            print(response)
        
        elif choice == '3':
            subject_name = input("Enter subject name: ").strip()
            raw_input = input("Enter percentage mark (0-100): ").strip()
            try:
                percentage_mark = float(raw_input)
                if 0 <= percentage_mark <= 100:
                    # FIXED: Pass raw_input string so Layer 2 handles parsing exactly as designed!
                    response = log_raw_score(test_ib_profile, subject_name, raw_input)
                    print(response)
                else:
                    print("Error: Score must be between 0 and 100.")
            except ValueError:
                print("Error: Numeric input required.")
        
        elif choice == '4':
            tok_grade = input("Enter TOK grade (A-E): ").strip()
            ee_grade = input("Enter EE grade (A-E): ").strip()
            response = update_core_points(test_ib_profile, tok_grade, ee_grade)
            print(response)
        
        elif choice == '5':
            if len(test_ib_profile) <= 1:
                print("\n⚠️ No subjects registered yet.")
            else:
                subject_name = input("Enter subject name to remove: ").strip().title()
                if subject_name in test_ib_profile and subject_name != "core_bonus":
                    del test_ib_profile[subject_name]
                    save_ib_data_to_file(test_ib_profile)
                    print(f"Subject '{subject_name}' has been removed successfully!")
                else:
                    print(f"Subject '{subject_name}' was not registered.")
        
        elif choice == '6':
            print("Exiting IB Grade Tracker. Goodbye!")
            break
        
if __name__ == "__main__":
    main()
                
               
                

                                                             
                    
            

        




            

           
                  









        

        
