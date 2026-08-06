# Defining the book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


# Defining the patron class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book in self.borrowed_books:
            return False
        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False


# Defining the library class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron

    def borrow_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return False

        if isbn not in self.books:
            print("Book not found.")
            return False

        book = self.books[isbn]
        patron = self.patrons[patron_id]

        if not book.borrow():
            print(f"Sorry, '{book.title}' is already borrowed.")
            return False

        if not patron.borrow_book(book):
            book.return_book()
            print(f"{patron.name} already has this book.")
            return False

        print(f"Success! {patron.name} borrowed '{book.title}'.")
        return True

    def return_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return False

        if isbn not in self.books:
            print("Book not found.")
            return False

        book = self.books[isbn]
        patron = self.patrons[patron_id]

        if not patron.return_book(book):
            print(f"{patron.name} did not borrow '{book.title}'.")
            return False

        book.return_book()
        print(f"Success! {patron.name} returned '{book.title}'.")
        return True


# Example usage
if __name__ == "__main__":
    library = Library()
    book = Book("Python Basics", "John Doe", "B001")
    patron = Patron("Alice", "P001")

    library.add_book(book)
    library.register_patron(patron)

    library.borrow_book("P001", "B001")
    library.return_book("P001", "B001")
