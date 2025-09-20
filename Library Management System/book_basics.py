class Book:
    """
    A class that presents a book with a title and an author.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book object.

        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a formatted string representation of the Book object.
        """
        return (f"\nMy favorite book is: {self.title} by {self.author}\n")

# Create an instance of the Book class
my_favorite_book = Book("Lord of the Rings", "J. R. R. Tolkien")

# Print the book object, which will use the __str__ method
print(my_favorite_book)