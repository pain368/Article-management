from flask import Flask, render_template, request, url_for, sessions, redirect

from flask_session import Session
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "12345"



class MyForm(FlaskForm):
    name = StringField("Login", validators=[DataRequired()])
    password = PasswordField("Haslo", validators=[DataRequired()])
    submit = SubmitField("Zaloguj")


@app.route("/", methods=("GET", "POST"))
def index():

    myform = MyForm()

    if myform.validate_on_submit():

        login = myform.name.data
        password = myform.password.data

        return redirect(login)

    else:

        return render_template("index.html", form = MyForm())


@app.route('/<username>', methods=["GET", "POST"])
def login(username=MyForm.name):

    return render_template("dashboard.html", username=username)


@app.route('/<username>/management_article', methods=["GET", "POST"])
def management_article(username):
    return render_template('management_article.html')


if __name__ == "__main__":

    app.run(debug=True)