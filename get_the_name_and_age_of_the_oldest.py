def is_valid_name(name):
    return name.isalpha() and len(name) 

def main():
    individuals = {} # Initialize individuals as an empty dictionary

    #  Loop: asks the user to input
    while True:
        name = input("Enter your name: ")
        if not is_valid_name(name):
            print("Error! Invalid name. Please enter a valid name (letters only).")
            continue

        age = int(input("Enter your age: "))
        try: 
            if age < 0 and age > 100:
                raise ValueError("Age must be between 0 and 100")
        except ValueError as e:
            print(f"Error! {e} Please enter a valid age")
            continue

