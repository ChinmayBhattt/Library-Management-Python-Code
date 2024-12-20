import datetime

# Book class to manage individual book details
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

# Library class to manage the library system
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        new_book = Book(title, author, copies)
        self.books.append(new_book)
        print(f'Book "{title}" added successfully!')

    def display_books(self):
        print("\nAvailable Books in Library:")
        for index, book in enumerate(self.books):
            print(f"{index + 1}. {book.title} by {book.author} ({book.copies} copies available)")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f'You have borrowed "{book.title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f'Thank you for returning "{book.title}".')
                return
        print(f'"{title}" is not a part of our library.')

# Main function
def main():
    library = Library()
    print("Welcome to the Library Management System!")

    while True:
        print("\nOptions:")
        print("1. Add a Book")
        print("2. Display Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            copies = int(input("Enter the number of copies: "))
            library.add_book(title, author, copies)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter the book title to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter the book title to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
