from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path, PurePath

sqlite_directory = Path(__file__).parent.absolute()
sqlite_file = PurePath(sqlite_directory, "books-collection.db")
all_books_list = []

def all_books():
    all_books = db.session.query(Book).all()
    return all_books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_file}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), unique=False, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

db.create_all()

@app.route('/')
def home():
    return render_template("index.html", books=all_books())


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")

        book = {
            "title": title,
            "author": author,
            "rating": rating
        }

        all_books_list.append(book)
        book = Book(title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()

        response = redirect(url_for("home"))
    else:
        response = render_template("add.html")
    return response

@app.route("/edit/<int:id>", methods = ["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book_to_update = Book.query.get(id)
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")

        book_to_update.title = title
        book_to_update.author = author
        book_to_update.rating = rating
        db.session.commit() 

        response = redirect(url_for("home"))
    else:
        book = Book.query.filter_by(id=id).first()
        response = render_template("edit.html", id=id, title=book.title, author=book.author, rating=book.rating)
    return response

@app.route("/delete/<int:id>", methods = ["POST"])
def delete(id):
    book_id = id
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    response = redirect(url_for("home"))

    return response


if __name__ == "__main__":
    app.run(debug=True)

