from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.isbn = isbn
    
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    def display_info(self):
        print(f'Judul Buku : {self.title}')
        print(f'Pengarang : {self.author}')
        print(f'No ISBN : {self.isbn}')

class FictionBook(Book):
    def __init__(self, title, author, isbn, genre) -> None:
        super().__init__(title, author, isbn)
        self.genre = genre
    
    def borrow(self):
        print(f'Borrow Book {self.title} by {self.author} ....')
    
    def return_book(self):
        print(f'returning {self.title} by {self.author}')
    
    def display_info(self):
        super().display_info()
        print(f'Genre : {self.genre}')

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, subject) -> None:
        super().__init__(title, author, isbn)
        self.subject = subject
    
    def borrow(self):
        print(f'Borrow Book {self.title} by {self.author}')
    
    def return_book(self):
        print(f'returning {self.title} by {self.author}')
    
    def display_info(self):
        super().display_info()
        print(f'Subject : {self.subject}')

def manage_book(book):
    book.borrow()
    book.display_info()
    book.return_book()

fiksi = FictionBook('The Hobbit', 'J.R.R Tolkien', '978-0261103283', 'Fantasy')
non_fiksi = NonFictionBook('A brief history of time', 'Stephan Hawking', '978-0553380163', 'Science')

print('Fiction Book :')
manage_book(fiksi)
print('')
print('Non Fiction Book :')
manage_book(non_fiksi)