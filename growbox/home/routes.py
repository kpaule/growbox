from growbox.models import HumidityFloor, HumidityWall, TemperatureFloor, TemperatureWall
from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")

