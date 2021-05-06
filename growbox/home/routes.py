from growbox.models import Metric
from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route('/dashboard/')
@login_required
def dashboard():
    metrics = Metric.query.all()
    metrics_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in metrics]
    return render_template("dashboard.html",
                           metrics=metrics,
                           metrics_date=metrics_date)


