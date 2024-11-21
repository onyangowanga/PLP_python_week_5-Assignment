# Base class of Books

# Create a class representing Books
class Book:
    def __init__(self, title, author, genre, pages):
        # Add attributes
        self.title = title        
        self.author = author
        self.genre = genre
        self.pages = pages

    # add method
    def read(self):
        print(f"Reading '{self.title}' by {self.author}...")

    # Use constructors
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"


# Derived class - Inheritance
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_format):
        super().__init__(title, author, genre, pages)  # Inherited attributes from the parent class
        self.file_format = file_format        # New attribute specific to EBooks
    
    # add method
    def download(self):
        print(f"Downloading '{self.title}' in {self.file_format} format...")
    
    # Polymorphism: Overriding the __str__ method
    def __str__(self):
        return f"{super().__str__()}, Format: {self.file_format}"


# Instantiate objects from both classes
book1 = Book("The Great Controversy", "E. G. White", "Prophecy", 650)
ebook1 = EBook("The Two Babylons", "Alexander Hyslop", "Historical", 250, "EPUB")

# Demonstrating Encapsulation, Inheritance, and Polymorphism
# Displays base class info
print(book1)  
book1.read()

# Displays inherited and extended class info
print(ebook1)  
ebook1.read()
ebook1.download()
