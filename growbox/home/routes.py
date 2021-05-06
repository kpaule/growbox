from datetime import datetime, timedelta

from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import desc

from growbox.models import Metric

home = Blueprint("home", __name__)


@home.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")


@home.route("/dashboard/now/")
@login_required
def dashboard_now():
    metric = Metric.query.order_by(desc(Metric.id)).first()
    return metric.as_dict()


@home.route("/dashboard/<string:time>/<int:amount>/", methods=["GET", "POST"])
@login_required
def dashboard_time(time, amount):
    before_time = datetime.utcnow() - timedelta(**{time: amount})
    metrics = Metric.query.filter(Metric.date >= before_time).all()
    result = {}
    for i, m in enumerate(metrics):
        result[i] = m.as_dict()
    return result
