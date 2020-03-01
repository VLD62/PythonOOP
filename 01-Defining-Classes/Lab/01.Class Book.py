class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = int(pages)

if __name__ == "__main__":
    book = Book("My Book", "Me", 200)
    print(book.name)
    print(book.author)
    print(book.pages)
