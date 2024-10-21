def is_valid_name(name): # This function checks if a given name is valid
    return name.isalpha() and len(name)  # Checks if the name contains only alphabetic characters and not empty

def main():
    individuals = {} # Initialize individuals as an empty dictionary

    #  Loop: Asks the user to input
    while True:
        name = input("Enter your name: ")
        if not is_valid_name(name): # Checks if the name is valid using is_valid_name()
            print("Error! Invalid name. Please enter a valid name (letters only).")
            continue

        age = int(input("Enter your age: "))
        try: # Used to catch potential errors
            if age < 0 or age > 100:  
                raise ValueError("Age must be between 0 and 100")
        except ValueError as e: # ValueError would be raised if the age is invalid
            print(f"Error! {e} Please enter a valid age")
            continue 

        individuals[name] = age  # If both name and age are valid, it adds the name and age to the individuals dictionary

        # Asking for another input
        another = input("Do you want to input another entry? (Yes/No): ").strip().lower() # The input is stripped of whitespace and converted to lowercase
        
        # If the user answers "no," the loop breaks; if "yes," it continues
        if another == "no": 
            break
        if another == "yes":
            continue

        # Summary of entries
        if individuals:
        oldest_name = max(individuals, key=individuals.get)  # finds the oldest person using max() with individuals.get to get the maximum age
        oldest_age = individuals[oldest_name]

        print("\n--- Summary of Entries ---") # Prints a summary of all entries, including the oldest person and their age
        for person, age in individuals.items():  # for loop iterates over all items in the individuals dictionary
            print(f"{person}: {age} years old")
                  
        print(f"\nThe oldest person is {oldest_name} with the age of {oldest_age}.")  # Finally, it prints out who the oldest person is along with their age





