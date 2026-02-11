class BookSystem:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = title

    def display_books(self):
        print(self.books)

    def update_book(self, book_id, new_title):
        if book_id in self.books:
            self.books[book_id] = new_title

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]


