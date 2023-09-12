import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = os.urandom(16)
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = EmailField(label="Email",
                       validators=[DataRequired(),
                                   Email(message="Invalid email address.")
                                   ]
                       )
    password = PasswordField(label="Password",
                             validators=[DataRequired(),
                                         Length(min=8, message="Field must be at least 8 characters long.")
                                         ]
                             )
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
