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
        return jsonify(books)
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