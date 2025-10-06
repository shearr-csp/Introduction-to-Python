# contact_manager.py

# Custom Exception
class DuplicateContactError(Exception):
    """Custom exception raised when attempting to add a contact that already 
    exists."""
    pass

# Initialize the contacts dictionary for the main application use
contacts = {}

# Core Contact Management Functions (Accepting dictionary for testability)

def add_contact(contacts_dict, name, phone):
    """
    Adds a contact to the dictionary.
    Raises DuplicateContactError if the contact already exists.
    """
    if name in contacts_dict:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    
    contacts_dict[name] = phone
    
    return contacts_dict

def find_contact(contacts_dict, name):
    """
    Finds a contact by name.
    Returns the phone number (string) if found, or None if not found.
    This function handles the lookup gracefully, making it easy to test.
    """
    try:
        return contacts_dict[name]
    except KeyError:
        return None

def delete_contact(contacts_dict, name):
    """
    Deletes a contact by name.
    Returns True if deleted, or False if the contact was not found.
    """
    try:
        del contacts_dict[name]
        return True
    except KeyError:
        return False

# Main Application Loop with Error Handling

def main():
    global contacts
    
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice_str = input("Enter your choice: ").strip()

        # Input Validation for Menu Choice
        try:
            choice = int(choice_str)
        except ValueError:
            print("Error: Invalid input. Please enter a number from 1 to 4.")
            continue # Go back to the start of the loop

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            try:
                add_contact(contacts, name, phone)
                print(f"Success: Added {name} to contacts.")
            # Custom Exception handling for DuplicateContactError
            except DuplicateContactError as e:
                print(f"Error: {e}")

        elif choice == 2:
            name = input("Enter name to find: ")
            phone = find_contact(contacts, name)
            if phone:
                print(f"Info: {name}'s phone number is: {phone}")
            else:
                print("Error: Contact not found.")

        elif choice == 3:
            name = input("Enter name to delete: ")
            if delete_contact(contacts, name):
                print(f"Success: Deleted {name}.")
            else:
                print("Error: Contact not found.")

        elif choice == 4:
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()