#!/usr/bin/python3
"""
This module contains the Book and Library classes for a simple library
management system.
"""

class Book:
    """
    Represents a book with a title, an author, and a checkout status.

    Public Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available.

        Returns:
            bool: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    Represents a library that manages a collection of Book objects.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by its title if it is available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """
        Returns a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                break

    def list_available_books(self):
        """Prints a list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")