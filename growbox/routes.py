from flask import Flask, flash, redirect, render_template
from flask.helpers import url_for

from growbox import app
from growbox.forms import LoginForm


@app.route('/')
@app.route('/index/')
@app.route('/home/')
def home():
    return render_template("index.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Hello {form.username.data}! You are now logged in.", "success")
        return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")
