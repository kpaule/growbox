import logging

from flask import Blueprint

from growbox import mqtt

mqtt_client = Blueprint("mqtt_client", __name__)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc != 0:
        logging.error(f"Connection to broker failed with code: {rc}")
    else:
        mqtt.subscribe("growboxhsalbsensors/#")


@mqtt.on_topic("growboxhsalbsensors/Bodenfeucht")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/Feuchwand")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/Tempwand")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/TempBoden")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/LED")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/Luefter")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/Pumpe")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")


@mqtt.on_topic("growboxhsalbsensors/Heizung")
def handle_topic_bodenfeucht(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

# For debugging
# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#    print(client, userdata, level, buf)
