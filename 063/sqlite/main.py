import sqlite3
from pathlib import Path, PurePath
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sqlite_directory = Path(__file__).parent.absolute()
sqlite_file_2 = PurePath(sqlite_directory, "new-books-collection.db")

def sqlite3_database_stuff():
    sqlite_file = PurePath(sqlite_directory, "books-collection.db")
    db = sqlite3.connect(sqlite_file)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()

def flask_database_stuff():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_file_2}"
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

    # Create
    book = Book(title="Harry Potter", author=". K. Rowling", rating=9.3)
    db.session.add(book)
    db.session.commit()

    # Read
    all_books = db.session.query(Book).all()
    book = Book.query.filter_by(title="Harry Potter").first()
    query = Book.query.filter(Book.title == "Harry Potter").all()
    print(query)

    # Update
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit() 

    # Delete
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
