
# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from webb_app.models import Book, db

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
@book_routes.route("/books_endpoint")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)


@book_routes.route("/books")
def list_books_for_humans():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]

    # SELECT * FROM books
    book_records = Book.query.all()
    print(book_records)

    return render_template("books.html", message="Here's some books", books=book_records)


@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")


@book_routes.route("/books/create", methods=["POST"])
def create_book():
    # Transforming the request.form into a dictionary 
    print("FORM DATA:", dict(request.form))

    # Creating a "new_book" instance 
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    # Adding the "new_book" instance to the DataBase
    db.session.add(new_book)
    # Committing the change to the DataBase
    db.session.commit()

    return jsonify({
        "message": "BOOK CREATED OK!",
        "book": dict(request.form)
    })
    
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    
    # Redirects you back to "books" page after creating new book
    # return redirect("/books")

