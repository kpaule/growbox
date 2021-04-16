import logging
import sys
from flask import Blueprint
from growbox import mqtt

mqtt_client = Blueprint("mqtt_client", __name__)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc != 0:
        logging.error(f"Connection to broker failed with code: {rc}")
    else:
        mqtt.subscribe("growbox/temp")
        mqtt.subscribe("growbox/humid")


@mqtt.on_message()
def handle_mqtt_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload), file=sys.stderr)
