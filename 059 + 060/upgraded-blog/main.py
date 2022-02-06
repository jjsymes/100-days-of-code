from flask import Flask, render_template, request
import smtplib
import requests
import os


FAKE_POSTS_ENDPOINT="https://api.npoint.io/627b3974afe367016b0f"
EMAIL_NOTIFICATION_TO=os.getenv("EMAIL_NOTIFICATION_TO")
EMAIL_NOTIFICATION_FROM=os.getenv("EMAIL_NOTIFICATION_FROM")
EMAIL_NOTIFICATION_FROM_PASSWORD=os.getenv("EMAIL_NOTIFICATION_FROM_PASSWORD")

def send_message(subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_NOTIFICATION_FROM, password=EMAIL_NOTIFICATION_FROM_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_NOTIFICATION_FROM,
            to_addrs=EMAIL_NOTIFICATION_TO,
            msg=f"Subject:{subject}\n\n{message}".encode('utf-8')
        )

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

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        response = render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        if EMAIL_NOTIFICATION_TO and EMAIL_NOTIFICATION_FROM and EMAIL_NOTIFICATION_FROM_PASSWORD:
            subject = f"Message from {name}"
            email_content = f"From: {name}\nEmail: {email}\nPhone: {phone}\n Message:\n\n{message}"
            send_message(subject, email_content)
            heading = "Successfully sent message"
        else:
            heading="Could not send message"
        response = render_template("contact.html", heading=heading)
    return response

@app.route('/post/<int:id>')
def post(id):
    posts = requests.get(FAKE_POSTS_ENDPOINT).json()
    post = next((post for post in posts if post["id"] == id), None)
    post.update({"author": "Josh"})
    post.update({"dates": "unknown date"})
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
