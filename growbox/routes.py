from flask import flash, redirect, render_template, request
from flask.helpers import url_for
from flask_login import current_user, login_required, login_user, logout_user

from growbox import app, bcrypt
from growbox.forms import LoginForm
from growbox.models import User


@app.route('/')
@app.route('/index/')
@app.route('/home/')
def home():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("dashboard"))
        else:
            flash(f"Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")
