# Robust Contact Manager
## Project Overview
This program built in Python is designed to be a simply command-line-based 
contact Management application. It has a robust error handling, input 
validation, and custom exceptions. 

## Features and Bug Fixes Implemented

The following improvements were made to the original program 
(`buggy_contacts.py`) to create the stable `contact_manager.py` application:

| **Bug** | **Fix** | 
| ----- | ----- | 
| **Program Crash on Missing Contact (Find/Delete)** | Implemented `try/except KeyError` blocks in both `find_contact` and `delete_contact` to gracefully handle lookups and deletions of non-existent names. | 
| **Duplicate Contacts Allowed** | Created the custom exception **`DuplicateContactError`**. The `add_contact` function now checks for existing contacts and explicitly `raise`s this error. The `main` function catches this error to inform the user. | 
| **Program Crash on Invalid Menu Input** | Implemented a `try/except ValueError` block in the `main` loop to handle non-integer input when the user selects a menu option, prompting them to try again instead of crashing. | 

## How to Run the Program
1. To run this program: Ensure that you have Python 3 installed on your system.
2. Clone repository: Clone this repository to your local computer using Git.
   - git clone [https://github.com/shearr-csp/Introduction-to-Python/tree/main/Robust%20Contact%20Manager]
3. Navigate to the project directory:
   - cd `Introduction-to-Python/Robust Contact Manager`
      - You might need to put "" around Robust Contact Manager if you get 
        the "too many arguments" error. 
4. Run the main program:
   - `python3 contact_manager.py`
      - The program will display a menu, allowing you to interactively add, 
      find, and delete contacts.

## How to Run the Unit Tests (Test Demonstration)

The `test_contact_manager.py` file uses `unittest` to verify all functionality.

To run the full test suite:

1. Open your terminal or command prompt.

2. Execute the `unittest` module against the test file:
   - `python3 -m unittest test_contact_manager.py`

### Purpose of Key Tests

The test suite ensures the application is robust:

   - **`test_add_duplicate_contact_raises_error`**: Verifies that the custom 
   `DuplicateContactError` is correctly raised when a name already exists.
   - **`test_find_non_existent_contact`**: Confirms that the `find_contact` 
   function handles a missing `KeyError` gracefully by returning `None`, 
   ensuring the application doesn't crash during a failed lookup.
   - **`test_delete_non_existent_contact`**: Ensures that attempts to delete a 
   contact not present in the dictionary are handled gracefully, returning 
   `False`.


