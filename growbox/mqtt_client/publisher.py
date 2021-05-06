import json

from flask import current_app
from growbox import create_app, mqtt

with create_app().app_context():
    topic_ctrl = current_app.config["MQTT_TOPIC"]


def set_led(status: bool):
    if status:
        mqtt.publish(topic_ctrl, json.dumps({"LED": "on"}))
    else:
        mqtt.publish(topic_ctrl, json.dumps({"LED": "off"}))


def set_fan(status: bool):
    if status:
        mqtt.publish(topic_ctrl, json.dumps({"Luefter": "on"}))
    else:
        mqtt.publish(topic_ctrl, json.dumps({"Luefter": "off"}))


def set_pump(status: bool):
    if status:
        mqtt.publish(topic_ctrl, json.dumps({"Pumpe": "on"}))
    else:
        mqtt.publish(topic_ctrl, json.dumps({"Pumpe": "off"}))


def set_heating(status: bool):
    if status:
        mqtt.publish(topic_ctrl, json.dumps({"Heizung": "on"}))
    else:
        mqtt.publish(topic_ctrl, json.dumps({"Heizung": "off"}))
