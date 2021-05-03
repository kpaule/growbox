from growbox.models import HumidityFloor, HumidityWall, TemperatureFloor, TemperatureWall
from flask import Blueprint, render_template
from flask_login import login_required

home = Blueprint("home", __name__)


@home.route('/dashboard/')
@home.route('/dashboard/overview/')
@login_required
def dashboard():
    temp_floor = TemperatureFloor.query.all()
    temp_floor_data = [x.temperature for x in temp_floor]
    temp_floor_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in temp_floor]
    temp_wall = TemperatureWall.query.all()
    temp_wall_data = [x.temperature for x in temp_wall]
    temp_wall_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in temp_wall]
    humi_floor = HumidityFloor.query.all()
    humi_floor_data = [x.humidity for x in humi_floor]
    humi_floor_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in humi_floor]
    humi_wall = HumidityWall.query.all()
    humi_wall_data = [x.humidity for x in humi_wall]
    humi_wall_date = [x.date.strftime("%A, %d. %B %Y %I:%M%p") for x in humi_wall]
    return render_template("dashboard_overview.html",
                           temp_floor_data=temp_floor_data,
                           temp_floor_date=temp_floor_date,
                           temp_wall_data=temp_wall_data,
                           temp_wall_date=temp_wall_date,
                           humi_floor_data=humi_floor_data,
                           humi_floor_date=humi_floor_date,
                           humi_wall_data=humi_wall_data,
                           humi_wall_date=humi_wall_date)


@home.route('/dashboard/temperature/')
@login_required
def dashboard_temperature():
    return render_template("dashboard_temperature.html")


@home.route('/dashboard/humidity/')
@login_required
def dashboard_humidity():
    return render_template("dashboard_humidity.html")
