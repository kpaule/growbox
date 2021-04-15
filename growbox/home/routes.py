from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint("home", __name__)

@home.route('/dashboard/')
@home.route('/dashboard/overview/')
@login_required
def dashboard():
    return render_template("dashboard_overview.html")

@home.route('/dashboard/temperature/')
@login_required
def dashboard_temperature():
    return render_template("dashboard_temperature.html")

@home.route('/dashboard/humidity/')
@login_required
def dashboard_humidity():
    return render_template("dashboard_humidity.html")
