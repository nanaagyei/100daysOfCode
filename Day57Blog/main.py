from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
posts = all_posts.json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", posts=posts, id=id)


if __name__ == "__main__":
    app.run(debug=True)
