# Library-Management-Python-Code
class Library:
    def __init__(self,ListOfBooks):
        self.books = ListOfBooks
    def DisplayAvailableBooks(self):
        print("The books present in this library are :")
        for book in self.books:
            print("*" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"Your Have been issued {bookName} Please Keep it Safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry This book already been issued")
            return False

    def retrunBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book")

class Student:
    def requestBook(self):
        reqBook = input("Enter The name of The Bookyou want to borrow")
        self.book =reqBook
        return self.book

    def returnBook(self):
        reqBook = input("Enter The name of The Book you want to return")
        self.book = reqBook
        return self.book
if __name__ == "__main__":
    centraLibrary = Library(["Algorithms","Django","Clrs","Python Notes"])
    Student = Student()
    # centraLibrary.DisplayAvailableBooks()
    while(True):
        welcomeMSG = '''=========Welcome To Central Library=========
        Please Choose an Option:
        1.List All book
        2.Request a Book
        3.Return a Book
        4.Exit The Library'''
        print(welcomeMSG)
        a = int(input("Enter a Choice\n-> "))
        if a==1:
            centraLibrary.DisplayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook()
        elif a==3:
            centraLibrary.retrunBook()
        elif a==4:
            exit()
        else:
            print("Invalid Choice")
