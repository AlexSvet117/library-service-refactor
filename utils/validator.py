from db import book_data

def validate_book_input(data):
    if not data.get("book_id"):
        return {"book_id": "book_id is required"}
    if not data.get("title"):
        return {"title": "title is required"}
    if not data.get("author"):
        return {"author": "author is required"}
        
    if not isinstance(data.get("book_id"), str):
        return {"book_id": "book_id should be str"}
    if not isinstance(data.get("title"), str):
        return {"title": "title should be str"}
    if not isinstance(data.get("author"), str):
        return {"author": "author should be str"}

    for book in book_data:
        if book.book_id == data.get("book_id"):
            return {"book_id" : f"book_id {data.get("book_id")} already exist"}