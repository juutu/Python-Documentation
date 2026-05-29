import json
import os

# GLOBAL CONFIGURATION
script_dir = os.path.dirname(os.path.abspath(__file__))
formulas_file = os.path.join(script_dir, 'formula_vault.json')

# LAYER 1: DATA PERSISTENCE (JSON File Storage)
# =====================================================================
def load_vault_from_file():
    if os.path.exists(formulas_file):
        with open(formulas_file, 'r') as file:
            return json.load(file)

    # Initialization Fallback
    seed_vault = {
        "Mechanics": {
            "Velocity": "v = s / t",
            "Acceleration": "a = (v - u) / t",
            "Newton's Second Law": "F = m * a"
        }
    }
    save_vault_to_file(seed_vault)
    return seed_vault

def save_vault_to_file(vault_data):
    with open(formulas_file, 'w') as file:
        json.dump(vault_data, file, indent=4)

# LAYER 2: LAB FUNCTIONS (CORE LOGIC RULES)
# =====================================================================
def add_formula(vault, topic, formula_name, equation):
    topic = topic.title().strip()
    formula_name = formula_name.title().strip()
    equation = equation.strip()

    if not topic:
        return "Error: Topic cannot be empty!"

    if not formula_name:
        return "Error: Formula name cannot be empty!"
    
    if topic not in vault:
        vault[topic] = {}

    if formula_name in vault[topic]:
        return f"Error: Formula '{formula_name}' already exists in topic '{topic}'. Cannot add duplicates!"
    
    vault[topic][formula_name] = equation
    save_vault_to_file(vault)
    return f"Success: Formula '{formula_name}' saved to Topic '{topic}' successfully!" 

def remove_formula(vault, topic, formula_name):
    topic = topic.title().strip()
    formula_name = formula_name.title().strip()

    if topic not in vault:
        return f"Error: Topic '{topic}' was not found in the vault."
    if formula_name not in vault[topic]:
        return f"Error: Formula '{formula_name}' not found under Topic '{topic}'."

    del vault[topic][formula_name]
    save_vault_to_file(vault)
    return f"Success: Formula '{formula_name}' removed from Topic '{topic}' successfully!"

def search_formulas(vault, keyword):
    keyword = keyword.lower().strip()

    search_results = {}

    for topic, formulas in vault.items():
        for formula_name, equation in formulas.items():
            # Check if keyword is in topic or formula name (lowercased for matching)
            if keyword in topic.lower() or keyword in formula_name.lower():
                if topic not in search_results:
                    search_results[topic] = {}
                search_results[topic][formula_name] = equation

    if not search_results:
        return f"No matching formulas found for query: '{keyword}'"
    
    return search_results

# LAYER 3: TERMINAL INTERFACE (USER MENU LOOP)
# =====================================================================
def main():
    test_vault = load_vault_from_file()

    while True:
        print("=== IB Formula Vault Dashboard ===")
        print("1. View All Formulas")
        print("2. Add a New Formula Entry ")
        print("3. Remove a Formula Entry")
        print("4. Search Formulas by Keyword")
        print("5. Exit Program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if len(test_vault) == 0:
                print("\n⚠️ No formulas saved yet. Please add a formula first!")
            else:
                for topic, formulas in test_vault.items():
                    # Print Topic with decorative borders
                    print(f"\n{'='*10} {topic.upper()} {'='*10}")
                    # Nested loop for indented equations
                    for name, eq in formulas.items():
                        print(f"  -> {name}: {eq}")
        elif choice == '2':
            topic = input("Enter topic: ")
            formula_name = input("Enter formula name: ")
            equation = input("Enter formula equation: ")

            result = add_formula(test_vault, topic, formula_name, equation)  
          
            print(result)
        
        elif choice == '3':
            topic = input("Enter topic: ")
            formula_name = input("Enter formula name: ")

            result = remove_formula(test_vault, topic, formula_name)
            print(result)
        
        elif choice == '4':
            keyword = input("Enter keyword to search: ")

            result = search_formulas(test_vault, keyword)
            
            if isinstance(result, str):
                print(result)
            
            else:
                print(f"\n--- Search Results for '{keyword}' ---")

                for topic_name, formula_dict in result.items():
                    print(f"\nTopic: [{topic_name}]")
                    for formula_name, equation in formula_dict.items():
                        print(f"  -> {formula_name}: {equation}")
                    print("\n------------------------------------")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please choose an option between 1 and 5.")

if __name__ == "__main__":
    main()


        




            


        



                



            

















            




        


















    


    

    


        
