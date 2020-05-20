class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #se pueden redfinir metodos para el uso con objetos.
    def __str__(self):
        return f'The title is {self.title} and the author is {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("The book has been deleted")

book1 = Book('Python', 'Nacho222', 200)

print(book1)

print("tamaño del libro : "+ str(len(book1)))