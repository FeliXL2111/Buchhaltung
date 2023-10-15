from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("present_page/index.html", name="Tim")

@views.route("/profile/<username>")
def profile(username):
    return render_template("present_page/index.html", name=username)

@views.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login/login.html")