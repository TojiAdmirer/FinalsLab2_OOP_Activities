class BookPages:
    def __init__(self, book_pages):
        self.book_pages = book_pages

    def __str__(self):
        return str(self.book_pages) + " pages"

    def __add__(self, other):
        return BookPages(self.book_pages + other.book_pages)

book1 = BookPages(120)
book2 = BookPages(85)

print(book1)
combined = book1 + book2
print(combined)