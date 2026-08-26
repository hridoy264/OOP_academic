class Book:
    def __init__(self, title = None, author = None):
        self.title = title
        self.author = author

        print(f"{self.title}: {self.author}")

book1 = Book()
book2 = Book("The Hobbit")
book3 = Book("La Miserable", "Victor Hugo")

