from flask import Flask, jsonify, render_template, request
from controllers.book_controller import book_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp)
    return app




if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)