from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0,9)

choice_html = "<p><a href=\"/\">Reset Game</a> <a href=\"/0\">0</a> <a href=\"/1\">1</a> <a href=\"/2\">2</a> <a href=\"/3\">3</a> <a href=\"/4\">4</a> <a href=\"/5\">5</a> <a href=\"/6\">6</a> <a href=\"/7\">7</a> <a href=\"/8\">8</a> <a href=\"/9\">9</a></p>"

@app.route("/")
def home():
    global number 
    number = randint(0,9)
    return "<h1>Guess a number between 0 and 9</h1>" \
        '<img height="500px" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Gif">' \
        f"{choice_html}"

@app.route("/<int:guess>")
def answer(guess):
    global number

    if guess > number:
        result = "Too high, try again!"
        img_src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
        color = "purple"
    elif guess < number:
        result = "Too low, try again!"
        img_src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
        color = "red"
    else:
        result = "You found me!"
        img_src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
        color = "green"

    return f'<h1 style="color:{color};">{result}</h1>' \
        f'<img height="500px" src="{img_src}" alt="Gif">' \
        f"{choice_html}"

if __name__ == "__main__":
    app.run()