from flask import Blueprint, jsonify, request
from services.book_service import BookService


book_bp = Blueprint("books", __name__, url_prefix="/v2")


@book_bp.route("/books", methods = ["GET"])
def get_books():
    books = BookService.get_all_books()
    return jsonify([book.to_dict() for book in books])

@book_bp.route("/books/<string:book_id>", methods = ["GET"])
def get_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error" : "Book not found"}), 404


@book_bp.route("/books", methods = ["POST"])
def add_book():
    data = request.json
    if not data:
        return jsonify({"error": "The payload can not be empty"}), 400
    books = BookService.create_book(data)
    if not isinstance(books, list):
        return jsonify(books), 400
    response = {"message" : "Book succesfully created",
                "books" : [book.to_dict() for book in books]}
    return jsonify(response)


@book_bp.route("/books/<string:book_id>", methods = ["DELETE"])
def delete_book(book_id):
    result, books = BookService.delete_book(book_id)
    
    if not result:
        return jsonify({"error": " Book not found"}), 404
    response = {"message" : f"Book with book id {book_id} sucessfully deleted",
                "books": [book.to_dict() for book in books]}
    return jsonify(response)


# @book_bp.route("/books/<string:book_id>", methods = ["PUT"])
# def update_book(book_id):

#     book_to_update = BookService.update_book(book_id)
#     if book_to_update:
#         new_book = request.json
#         book_to_update.update(new_book)
#         return jsonify({"status" : "Book successfully updated", "books" : [book.to_dict() for book in books]}), 201
#     return jsonify({"error": "Book not found"}), 400
    # if not book_to_update:
    #     return jsonify({"error": " Book not found"}), 404
    # return jsonify(book_to_update.to_dict(), "Book successfully updated"), 200

@book_bp.route("/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    if not data:
        return jsonify({"error": "The payload cannot be empty"}), 400
    
    updated_book = BookService.update_book(book_id, data)
    
    if isinstance(updated_book, dict) and "error" in updated_book:
        # If we get an error message from the service layer
        return jsonify(updated_book), 400
    
    return jsonify(updated_book.to_dict())