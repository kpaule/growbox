from flask import Blueprint, render_template
from flask_login import login_required
from growbox.models import Metric
from sqlalchemy import desc

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
