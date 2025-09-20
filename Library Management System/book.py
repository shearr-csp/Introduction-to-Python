class Book:
    """
    A class that presents a book with a title and an author.
    """
    def __init__(self, title, author, isbn):
        """
        Initializes a new Book object.

        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """
        Returns a formatted string representation of the Book object.
        """
        return (
            f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
    def get_details(self):
        """
        Returns the book's details.
        """
        return {
            "Title": self.title,
            "Author": self.author,
            "ISBN": self.isbn,
        }