class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"{self.name} by {self.author} and {self.pages} pages"

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

book1 = Book("My Book1", "Me1", 2001)

print(book)
print(book1)
