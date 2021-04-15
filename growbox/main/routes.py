from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from growbox import bcrypt
from growbox.main.forms import LoginForm
from growbox.models import User

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/index/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("home.dashboard"))
    else:
        return redirect(url_for("main.login"))


@main.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("home.dashboard"))
        else:
            flash(f"Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", form=form)


@main.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for("main.index"))
