from django.db import models

class Book:

    def __init__(self, isbn,title,year):
        self.isbn = isbn
        self.title = title
        self.year = year

class Library:

    def __init__(self) -> None:
        b1 = Book("asd1","The lor of the rings",1954)
        b2 = Book("asd2","The analyst",2002)

        self.book_list = [b1,b2]

    def add_book(self,book):
        if isinstance(book,Book):
            if book.isbn == "" or book.title == "" or book.year == "":
                return "Missing Book Data"
            else:
                for b in self.book_list:
                    if isinstance(b,Book):
                        if b.isbn == book.isbn:
                            return "The book is already in the library"
                    else:
                        return "This is not a book"
                self.book_list.append(book)
                return "Book added to library"
        else:
            return "Missing book data"
        
    def list_books(self):
        return self.book_list
    
    def delete_book(self,isbn):
        for b in self.book_list:
            try:
                if isinstance(b,Book):
                    if b.isbn == isbn:
                        self.book_list.remove(b)
                        return "Book deleted from library"
                else:
                    return "The isbn is not in library"
            except:
                return "An error has ocurred"

