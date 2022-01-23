import imp
from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

def current_year():
    return dt.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", current_year=current_year())

@app.route("/blog")
def blog():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=posts, current_year=current_year())

@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    nationality_response = requests.get(f"https://api.nationalize.io?name={name}").json()
    if nationality_response["country"]:
        nationality = nationality_response["country"][0]["country_id"]
    else:
        nationality = "Earth"
    return render_template("guess.html", name=name, age=age, gender=gender, nationality=nationality, current_year=current_year())

if __name__ == "__main__":
    app.run()
