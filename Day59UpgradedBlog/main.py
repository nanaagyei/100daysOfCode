from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/2ad8ecaddae227b32703")
posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Me")


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", post_id=post_id, posts=posts, title="Post")


if __name__ == "__main__":
    app.run(debug=True)

