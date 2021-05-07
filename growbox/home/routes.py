from datetime import datetime, timedelta

from flask import Blueprint, render_template, current_app
from flask_login import login_required
from sqlalchemy import desc, func

from growbox import create_app, db, mqtt
from growbox.models import Metric

home = Blueprint("home", __name__)
with create_app().app_context():
    topic_ctrl = current_app.config["MQTT_TOPIC_CTRL"]


@home.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")


@home.route("/dashboard/now/")
@login_required
def dashboard_now():
    metric = Metric.query.order_by(desc(Metric.id)).first()
    return metric.as_dict()


@home.route("/dashboard/day/")
@login_required
def dashboard_day():
    date_start = datetime.utcnow() - timedelta(hours=2)
    date_end = datetime.utcnow()

    avg_dict = {}

    for i in range(12):
        curr_avg_tuple = db.session.query(func.avg(Metric.temperature_air),
                                          func.avg(Metric.temperature_ground),
                                          func.avg(Metric.humidity_air),
                                          func.avg(Metric.humidity_ground)) \
            .filter(date_start < Metric.date) \
            .filter(Metric.date < date_end) \
            .first()
        curr_avg_dict = {
            "date_start": date_start,
            "date_end": date_end,
            "temperature_air": curr_avg_tuple[0],
            "temperature_ground": curr_avg_tuple[1],
            "humidity_air": curr_avg_tuple[2],
            "humidity_ground": curr_avg_tuple[3]
        }

        avg_dict[i] = curr_avg_dict

        date_start = date_start - timedelta(hours=2)
        date_end = date_end - timedelta(hours=2)

    return avg_dict


@home.route("/dashboard/<string:time>/<int:amount>/", methods=["GET", "POST"])
@login_required
def dashboard_time(time, amount):
    before_time = datetime.utcnow() - timedelta(**{time: amount})
    metrics = Metric.query.filter(Metric.date >= before_time).all()
    result = {}
    for i, m in enumerate(metrics):
        result[i] = m.as_dict()
    return result


@home.route("/dashboard/led/<int:status>/", methods=["GET", "POST"])
@login_required
def toggle_led(status):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"LED\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"LED\":\"off\"}")
    return '', 200


@home.route("/dashboard/pump/<int:status>/", methods=["GET", "POST"])
@login_required
def toggle_pump(status):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Pumpe\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Pumpe\":\"off\"}")
    return '', 200


@home.route("/dashboard/heating/<int:status>/", methods=["GET", "POST"])
@login_required
def toggle_heating(status):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Heizung\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Heizung\":\"off\"}")
    return '', 200


@home.route("/dashboard/fan/<int:status>/", methods=["GET", "POST"])
@login_required
def toggle_fan(status):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Luefter\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Luefter\":\"off\"}")
    return '', 200
