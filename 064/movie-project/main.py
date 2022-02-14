from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import CSRFProtect
from werkzeug.datastructures import MultiDict
from flask_bootstrap import Bootstrap
from models import Movie, db
from forms import MovieEditForm, MovieAddForm, MovieSelectForm
from movie_data import get_movie_metadata, search_movies
from pathlib import Path, PurePath

SQLITE_DIRECTORY = Path(__file__).parent.absolute()
SQLITE_FILE = PurePath(SQLITE_DIRECTORY, "movies.db")
SQLALCHEMY_DATABASE_URI=f"sqlite:///{SQLITE_FILE}"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect()

csrf.init_app(app)

Bootstrap(app)

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route("/")
def home():
    Movie.set_ranking()
    all_movies= db.session.query(Movie).order_by(Movie.rating.desc()).limit(10).all()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieAddForm()
    if form.validate_on_submit():
        title = form.title.data
        movies = search_movies(title)
        response = render_template("select.html", movies=movies, form=MovieSelectForm())
    else:
        response = render_template("add.html", form=form)
    return response


@app.route("/submit", methods=["POST"])
def submit():
    form = MovieSelectForm()
    if form.validate_on_submit():
        movie_id = form.id.data
        metadata = get_movie_metadata(movie_id)
        movie = Movie(
            title=metadata.get("title"),
            year=metadata.get("release_date"),
            description=metadata.get("overview"),
            img_url=f"https://image.tmdb.org/t/p/original/{metadata.get('poster_path')}"
        )
        db.session.add(movie)
        db.session.commit()
        response = redirect(url_for("edit", id=movie.id))
    return response


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    response = redirect(url_for("home"))
    return response


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    form = MovieEditForm()
    if not movie_id:
        response = redirect(url_for("home"))
    else:
        movie_to_update = Movie.query.get(movie_id)
        if form.validate_on_submit():
            new_rating = form.rating.data
            new_review = form.review.data
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit() 
            response = redirect(url_for("home"))
        else:
            if movie_to_update.rating:
                prefilled_rating = movie_to_update.rating
            else:
                prefilled_rating =  ""
            if movie_to_update.review:
                prefilled_review = movie_to_update.review
            else:
                prefilled_review =  ""
            form = MovieEditForm(formdata=MultiDict({"rating": prefilled_rating, "review": prefilled_review}))
            response = render_template("edit.html", form=form, movie=movie_to_update)
    return response

if __name__ == '__main__':
    app.run(debug=True)
