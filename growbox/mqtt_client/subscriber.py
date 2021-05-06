import json
import logging

from flask import current_app
from growbox import create_app, db, mqtt
from growbox.models import Metric

with create_app().app_context():
    topic = current_app.config["MQTT_TOPIC"]


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc != 0:
        logging.error(f"Connection to broker failed with code: {rc}")
    else:
        mqtt.subscribe(topic)


@mqtt.on_message()
def handle_message(client, userdata, message):
    print(f"Received message {message.payload.decode()}")
    data = json.loads(message.payload)

    metric = Metric()
    metric.humidity_ground = data.get("Bodenfeucht", 0.0)
    metric.humidity_air = data.get("Feuchwand", 0.0)
    metric.temperature_air = data.get("Tempwand", 0.0)
    metric.temperature_ground = data.get("TempBoden", 0.0)
    metric.light = True if data.get("LED") == "on" else False
    metric.fan = True if data.get("Luefter") == "on" else False
    metric.pump = True if data.get("Pumpe") == "on" else False
    metric.heating = True if data.get("Heizung") == "on" else False

    # outside an application context -> manually push a context
    with create_app().app_context():
        try:
            db.session.add(metric)
            db.session.commit()
        except Exception as e: print(e)

# For debugging
# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#    print(client, userdata, level, buf)
