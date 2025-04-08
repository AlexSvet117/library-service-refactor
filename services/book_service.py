from db import book_data
from models.book_model import Book


class BookService:
    
    @staticmethod
    def get_all_books():
        return book_data
    
    @staticmethod
    def get_book_by_id(book_id :str):
        for book in book_data:
            if book.book_id == book_id:
                return book
        return None
    
    @staticmethod
    def create_book(data : dict):
            
        new_book = Book(
            book_id = data.get("book_id"),
            title = data.get("title"),
            author = data.get("author"),
            publication_year = data.get("publication_year", 0),
            genre = data.get("genre", ""),
            read_status = data.get("read_status", "to-read"),
            rating = data.get("rating", 0.0),
            notes = data.get("notes", "")
        )

        book_data.append(new_book)
        return book_data


    @staticmethod
    def delete_book(book_id):
        for book in book_data:
            if book.book_id == book_id:
                book_data.remove(book)
                return True, book_data
        return False, None

