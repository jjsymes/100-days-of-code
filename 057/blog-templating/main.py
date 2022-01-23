from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def view_post(id):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post = next((post for post in posts if post["id"] == id), None)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
