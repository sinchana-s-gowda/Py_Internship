class LibrarySearch:
    def __init__(self):
        self.library = {}

    def add_book(self, book_id, title):
        self.library[book_id] = title

    def display_books(self):
        print(self.library)

    def update_book(self, book_id, new_title):
        if book_id in self.library:
            self.library[book_id] = new_title

    def delete_book(self, book_id):
        if book_id in self.library:
            del self.library[book_id]


library = LibrarySearch()
library.add_book(1, "XYZ")
library.add_book(2, "ABC")
library.display_books()
library.update_book(1, "Updated XYZ")
library.delete_book(2)
library.display_books()