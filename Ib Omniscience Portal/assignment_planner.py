import json
import os
# LAYER 1: DATA PERSISTENCE (JSON File Storage)
# =====================================================================
script_dir = os.path.dirname(os.path.abspath(__file__))
DB_FILE_1 = os.path.join(script_dir, 'assignments.json')

def load_assignments_from_file():
    if not os.path.exists(DB_FILE_1): 
        return {}
    try:
        with open(DB_FILE_1, 'r') as file:
            parsed_data = json.load(file)
            return parsed_data
    except json.JSONDecodeError:
        return {}
def save_assignments_to_file(tasks):
    with open(DB_FILE_1, 'w') as file:
        json.dump(tasks, file, indent=4)
# LAYER 2: LAB FUNCTIONS (CORE LOGIC RULES)
# =====================================================================
def add_assignment(tasks, name, details):
    lowercase_name = name.lower()

    if lowercase_name in tasks:
        return f"Assignment '{lowercase_name}' already exists! Cannot add a duplicate."
    
    tasks[lowercase_name] = {
        "due_date": details.get("due_date", "n/a"),
        "status": details.get("status", "not started").lower(),
    }

    save_assignments_to_file(tasks)
    return f"Assignment '{lowercase_name}' tracked successfully."

def update_assignment_status(tasks, name, field, val):
    lower_name = name.lower()
    lower_field = field.lower()

    if lower_name not in tasks:
        return f"Assignment '{lower_name}' not found! Cannot update a non-existent assignment."
    
    if lower_field == "status":
        val = val.lower()

    tasks[lower_name][lower_field] = val

    save_assignments_to_file(tasks)
    return f"Assignment '{lower_name}' detail '{lower_field}' updated to '{val}' successfully."

def delete_assignment(tasks, name):
    lower_name = name.lower()

    if lower_name not in tasks:
        return f"Assignment not found!"
    
    del tasks[lower_name]

    save_assignments_to_file(tasks)

    return f"Assignment '{lower_name}' deleted successfully!"

def view_assignments(tasks):
    if not tasks:
        return f"No assignments scheduled."
    
    output = "Current Assignments:\n"

    for name in sorted(tasks):
        details = tasks[name]
        capitalized_name = name.capitalize()

        output += f"Assignment Name: {capitalized_name}\n Due Date: {details['due_date']}\n Status: {details['status']}\n\n"

    return output

# LAYER 3: TERMINAL INTERFACE (USER MENU LOOP)
# =====================================================================
def main():
    test_assignment = load_assignments_from_file()

    while True:
        print("\nAssignment Planner Menu:")
        print("1. View Current Assignment")
        print("2. Add a New Assignment")
        print("3. Edit Assignment Details")
        print("4. Delete an Assignment")
        print("5. Exit Program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            result = view_assignments(test_assignment)
            print(result)

        elif choice == '2':
            user_title = input("Enter assignment title:")
            user_date = input("Enter due date (YYYY-MM-DD):")
            user_status = input("Enter status (Not started/In Progress/Completed):")

            response = add_assignment(test_assignment, user_title, {"due_date": user_date, "status": user_status})

            print(response)

        elif choice == '3':
            user_name = input("Enter the name of the assignment to edit:")
            user_field = input("Enter the field to update (due_date/status):")
            user_val = input("Enter the new value for the field:")

            update = update_assignment_status(test_assignment, user_name, user_field, user_val)
            print(update)

        elif choice == '4':
            user_name = input("Enter the name of the assignment you want to delete:")
            delete = delete_assignment(test_assignment, user_name)
            print(delete)

        elif choice == '5':
            print("Exiting Assignment Planner. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()



    
    


    


   





    

           
            
