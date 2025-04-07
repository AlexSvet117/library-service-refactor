from db import book_data
class BookService:
    
    @staticmethod
    def get_all_books():
        return book_data
    
    @staticmethod
    def get_product_by_id(book_id :str):
        for book in book_data:
            if book.book_id == book_id:
                return book
        return None