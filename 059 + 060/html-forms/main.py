from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    form = request.form
    username = form["username"]
    password = form["password"]
    return f"Hello, {username}. Your passsword is {password}"

if __name__ == "__main__":
    app.run(debug=True)
