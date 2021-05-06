import json

from flask import current_app
from growbox import create_app, mqtt

with create_app().app_context():
    topic_ctrl = current_app.config["MQTT_TOPIC_CTRL"]


def set_led(status: int):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"LED\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"LED\":\"off\"}")


def set_fan(status: int):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Luefter\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Luefter\":\"off\"}")


def set_pump(status: int):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Pumpe\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Pumpe\":\"off\"}")


def set_heating(status: int):
    if status == 1:
        mqtt.publish(topic_ctrl, "{\"Heizung\":\"on\"}")
    else:
        mqtt.publish(topic_ctrl, "{\"Heizung\":\"off\"}")
