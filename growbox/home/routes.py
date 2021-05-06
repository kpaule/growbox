from growbox.models import Metric
from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route('/dashboard/')
@home.route('/dashboard/overview/')
@login_required
def dashboard():
    metrics = Metric.query.all()
    metrics_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in metrics]
    return render_template("dashboard_overview.html",
                           metrics=metrics,
                           metrics_date=metrics_date)


@home.route('/dashboard/temperature/')
@login_required
def dashboard_temperature():
    return render_template("dashboard_temperature.html")


@home.route('/dashboard/humidity/')
@login_required
def dashboard_humidity():
    return render_template("dashboard_humidity.html")
