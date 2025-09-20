from book import Book

def add_book(library):
    """
    Prompts the user for book details, creates a Book object, 
    and adds to the library list.
    """
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    new_book = Book(title, author, isbn)
    library.append(new_book)
    print(f"Book '{title}' has been added to the library.")

def list_books(library):
    """
    Iterates through the library list and prints the detials of each book.
    """
    if not library:
        print("The library is empty.")
    else:
        print("\n-- Current Library Inventory ----")
        for book in library:
            print(book) # The __str__ method is called here automatically
        print("___________________________________")

def find_book(library, query):
    """
    Searches the library for a book matching the query by title or author. 
    Returns the found Book object or none if not found. 
    """
    for book in library:
        if (query.lower() in book.title.lower() or 
            query.lower() in book.author.lower()):
            return book
    return None

def main():
    """
    Main function to run the library management programs. 
    """
    my_library = []
    while True:
        print("\nLibrary Managment System Menu:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book by title or author")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(my_library)
        elif choice == '2':
            list_books(my_library)
        elif choice == '3':
            query = input("enter the title or author to search for: ")
            found_book = find_book(my_library, query)
            if found_book:
                print("\nBook Found:")
                print(found_book)
            else:
                print("No matching book found.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()