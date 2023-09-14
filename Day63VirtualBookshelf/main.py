from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        new_dict = {
            "title": title,
            "author": author,
            "rating": int(rating),
        }
        all_books.append(new_dict)
        return render_template("add.html")
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

