from db import book_data
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
        if not data.get("book_id"):
            return {"book_id": "book_id is required"}
        if not data.get("title"):
            return {"title": "title is required"}
        if not data.get("author"):
            return {"author": "author is required"}
        
        if isinstance(data.get("book_id"), str):
            return {"book_id": "book_id should be str"}
        if isinstance(data.get("title"), str):
            return {"title": "title should be str"}
        if isinstance(data.get("author"), str):
            return {"author": "author should be str"}
        
        for book in book_data:
            if book.book_id == data.get("book_id"):
                return {"book_id" : f"book_id {data.get("book_id")} already exist"}



