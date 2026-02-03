class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("title:", self.title)
        print("author:", self.author)

class IssuedBook(Book):
    def _init_(self, title, author, issued_to, issued_date):
        super()._init_(title, author)  
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        super().display_book_details()   
        print("Issued To:",self.issued_to)
        print("Issued Date:",self.issued_date)

obj =IssuedBook("python debugger","venson","xyz","3 feb 26")
obj.display_book_details()
obj.display_issued_book_details()