from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.fields import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "some secret string"
csrf = CSRFProtect(app)
Bootstrap(app)

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password (password)", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        authenticated = False
        if form.password.data == "12345678" and form.email.data == "admin@email.com":
            authenticated = True
        if authenticated:
            response = render_template('success.html')
        else:
            response = render_template('denied.html')
    else:
        response = render_template('login.html', form=form)
        
    return response


if __name__ == '__main__':
    app.run(debug=True)