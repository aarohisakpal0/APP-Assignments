
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        self.books.append(Book(title))

    def register_patron(self, name):
        self.patrons.append(Patron(name))

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron
        return None

    def borrow_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        book = self.find_book(book_title)

        if patron and book and not book.is_borrowed:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            return True
        return False

    def return_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        book = self.find_book(book_title)

        if patron and book and book in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            return True
        return False

    def display(self):
        print("\n" + "=" * 50)
        print("           LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("\n--- BOOK DETAILS ---")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"Book: {book.title} | Status: {status}")

        print("\n--- PATRON DETAILS ---")
        for patron in self.patrons:
            if patron.borrowed_books:
                books = ", ".join(book.title for book in patron.borrowed_books)
                print(f"Patron: {patron.name} | Borrowed: {books}")
            else:
                print(f"Patron: {patron.name} | Borrowed: None")

        print("\n" + "=" * 50)


def main():
    library = Library()

    print("=" * 50)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)

    # Input number of books
    number_of_books = int(input("\nEnter number of books: "))

    # Input book details
    for i in range(number_of_books):
        title = input(f"Enter title of book {i + 1}: ")
        library.add_book(title)

    # Input number of patrons
    number_of_patrons = int(input("\nEnter number of patrons: "))

    # Input patron details
    for i in range(number_of_patrons):
        name = input(f"Enter name of patron {i + 1}: ")
        library.register_patron(name)

    # Borrowing details
    borrow = input("\nDo you want to borrow a book? (yes/no): ").lower()

    if borrow == "yes":
        patron_name = input("Enter patron name: ")
        book_title = input("Enter book title to borrow: ")

        if library.borrow_book(patron_name, book_title):
            print("Book borrowed successfully.")
        else:
            print("Unable to borrow book.")

    # Returning details
    return_book = input("\nDo you want to return a book? (yes/no): ").lower()

    if return_book == "yes":
        patron_name = input("Enter patron name: ")
        book_title = input("Enter book title to return: ")

        if library.return_book(patron_name, book_title):
            print("Book returned successfully.")
        else:
            print("Unable to return book.")

    # Display all details at the end
    library.display()


if __name__ == "__main__":
    main()
