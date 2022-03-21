from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#Line below only required once, when creating DB. 
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    response = render_template("index.html")
    return response

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        response = redirect(url_for("secrets"))
    else:
        if request.method == "GET":
            response = render_template("register.html")
        elif request.method == "POST":
            email = request.form.get("email")
            name = request.form.get("name")
            password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

            if User.query.filter_by(email=email).first():
                flash("Email already registered.")
                response = redirect(url_for("register"))
            else:
                new_user = User(
                    email=email,
                    name=name,
                    password=password
                )

                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)

                response = redirect(url_for("secrets"))
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        response = redirect(url_for("secrets"))
    else:
        if request.method == "GET":
            response = render_template("login.html")
        elif request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()

            if user:
                password_correct = check_password_hash(pwhash=user.password, password=password)
                if password_correct:
                    login_user(user)
                    response = redirect(url_for("secrets"))
                else:
                    flash("Incorrect password.")
                    response = redirect(url_for("login"))
            else:
                flash("User does not exist.")
                response = redirect(url_for("login"))
    return response


@app.route("/secrets")
@login_required
def secrets():
    name=current_user.name
    return render_template("secrets.html", name=name)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
