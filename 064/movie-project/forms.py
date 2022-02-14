from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MovieEditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g 7.5", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class MovieAddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


class MovieSelectForm(FlaskForm):
    id = StringField("TMDB Movie ID", validators=[DataRequired()])
    submit = SubmitField("Submit")
