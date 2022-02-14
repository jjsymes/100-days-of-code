from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    rating = db.Column(db.Float(), unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(250), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=True)

    def __repr__(self):
        return '<Title %r>' % self.title

    @classmethod
    def set_ranking(cls):
        all_movies = db.session.query(cls).order_by(cls.rating.desc()).all()
        for ranking, movie in enumerate(all_movies):
            movie.ranking = ranking + 1
        db.session.commit() 
