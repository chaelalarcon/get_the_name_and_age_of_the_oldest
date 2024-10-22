def is_valid_name(name): # This function checks if a given name is valid
    return all(c.isalpha() or c in " -'" for c in name) and len(name) > 0  # Allow letters, spaces, hyphens, and apostrophes

def main():
    individuals = {} # Initialize individuals as an empty dictionary

    #  Loop: Asks the user to input
    while True:
        name = input("Enter your name: ")
        if not is_valid_name(name): # Checks if the name is valid using is_valid_name()
            print("Error! Invalid name. Please enter a valid name (letters, spaces, hyphens, and apostrophes are allowed).")
            continue

        # Try to get age input and validate
        try: 
            age_input = input("Enter your age: ") # Get input as a string
            age = int(age_input) # Attemp to convert into integer

            if age < 0 or age > 100:  
                raise ValueError("Age must be between 0 and 100")
        except ValueError: # ValueError would be raised if the age is invalid
            print("Error! Please enter a valid age (numbers only from 0-100).")
            continue 

        individuals[name] = age  # If both name and age are valid, it adds the name and age to the individuals dictionary

        # Asking for another input
        another = input("Do you want to input another entry? (Yes/No): ").strip().lower() # The input is stripped of whitespace and converted to lowercase
        
        # If the user answers "no," the loop breaks
        if another == "no": 
            break

    # Summary of entries
    if individuals:
        oldest_name = max(individuals, key=individuals.get)  # finds the oldest person using max() with individuals.get to get the maximum age
        oldest_age = individuals[oldest_name]

        print("\n--- Summary of Entries ---") # Prints a summary of all entries, including the oldest person and their age
        for person, age in individuals.items():  # for loop iterates over all items in the individuals dictionary
            print(f"{person}: {age} years old")
                  
        print(f"\nThe oldest person is {oldest_name} with the age of {oldest_age}.")  # Finally, it prints out who the oldest person is along with their age

    else:
        print("No entries were made.") # If individuals is empty, it informs the user that no entries were made

if __name__ == "__main__": # This checks if the script is being run directly (not imported), and if so, it calls the main() function to execute the program
    main()




