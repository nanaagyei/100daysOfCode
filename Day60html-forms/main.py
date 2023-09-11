import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "prince.agyei.tuffour@gmail.com"
MY_PASSWORD = os.environ["MY_PASSWORD"]
RECIPIENT = "nanakwameagyeituffour@gmail.com"

posts = requests.get("https://api.npoint.io/2ad8ecaddae227b32703").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_msg(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_msg(name, email, phone, message):
    message = f"Name: {name}\n" \
              f"Email: {email}\n" \
              f"Phone: {phone}\n" \
              f"Message: {message}"
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = RECIPIENT
    msg['Subject'] = "New flight deal alert!"
    msg.attach(MIMEText(message, 'plain', 'utf-8'))  # Use 'plain' for plain text email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg=msg.as_string()  # Convert the MIMEText object to a string
        )


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
