from flask import Flask, render_template
import requests


FAKE_POSTS_ENDPOINT="https://api.npoint.io/627b3974afe367016b0f"

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get(FAKE_POSTS_ENDPOINT).json()
    for post in posts:
        post.update({"author": "Josh"})
        post.update({"dates": "unknown date"})
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    posts = requests.get(FAKE_POSTS_ENDPOINT).json()
    post = next((post for post in posts if post["id"] == id), None)
    post.update({"author": "Josh"})
    post.update({"dates": "unknown date"})
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
