from flask import Flask, render_template, redirect, url_for, flash, current_app
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "NOTSOSECRET")
ckeditor = CKEditor(app)
gravatar = Gravatar(app, size=200, rating='x', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLES

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="parent_post")

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('blog_posts.id'))
    author = relationship("User", back_populates="comments")
    parent_post = relationship("BlogPost", back_populates="comments")

db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def admin_only(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif current_user.id != 1:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return decorated_view


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        response = redirect(url_for("get_all_posts"))
    else:
        form = RegisterForm()
        if form.validate_on_submit():
            email=form.email.data
            name=form.name.data
            password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)

            if User.query.filter_by(email=email).first():
                flash("Email already registered. Log in instead.")
                response = redirect(url_for("login"))
            else:
                new_user = User(
                    email=email,
                    name=name,
                    password=password,
                )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                response = redirect(url_for("get_all_posts"))
        else:
            response = render_template("register.html", form=form)
    return response


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        response = redirect(url_for("get_all_posts"))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            email=form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user:
                password_correct = check_password_hash(pwhash=user.password, password=password)
                if password_correct:
                    login_user(user)
                    response = redirect(url_for("get_all_posts"))
                else:
                    flash("Incorrect password.")
                    response = redirect(url_for("login"))
            else:
                flash("User does not exist.")
                response = redirect(url_for("login"))

        else:
            response = render_template("login.html", form=form)
    return response


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            body=form.body.data
            comment = Comment(
                text=body,
                author=current_user,
                parent_post=requested_post
            )
            db.session.add(comment)
            db.session.commit()
            response = redirect(url_for("show_post", post_id=post_id))
        else:
            flash("You need to be logged in to comment.")
            response = redirect(url_for("login"))
    else:
        response = render_template("post.html", post=requested_post, form=form)
    return response


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@login_required
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@login_required
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@login_required
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
