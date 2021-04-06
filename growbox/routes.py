from flask import Flask, render_template
from growbox import app

@app.route('/')
@app.route('/index/')
@app.route('/home/')
def home():
    return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")