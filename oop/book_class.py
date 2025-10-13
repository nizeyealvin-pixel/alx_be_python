class Book:
    """A class representing a book with title, author, and publication year."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor called when the object is deleted.
        Prints a deletion message with the book's title.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return a human-readable string representation of the book.
        
        Returns:
            str: A formatted string describing the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return an official string representation that can recreate the object.
        
        Returns:
            str: A string that represents the Book constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"