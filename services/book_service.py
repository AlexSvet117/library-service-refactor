from db import book_data
class BookService:
    
    @staticmethod
    def get_all_books():
        return book_data