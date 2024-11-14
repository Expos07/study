class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            print("This book is already checked out.")
        else:
            self.is_checked_out = True
            print("The book has been checked out.")

    def return_book(self):
        if not self.is_checked_out:
            print("This book was not checked out.")
        else:
            self.is_checked_out = False
            print("The book has been returned.")

    def show_info(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "1234567890")

book.show_info()
book.check_out()
book.show_info()
book.return_book()
book.show_info()