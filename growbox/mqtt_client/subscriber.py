import json
import logging

from growbox import mqtt


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc != 0:
        logging.error(f"Connection to broker failed with code: {rc}")
    else:
        mqtt.subscribe("growboxhsalbsensors")


@mqtt.on_message()
def handle_message(client, userdata, message):
    print(f"Received message {message.payload.decode()}")
    data = json.loads(message.payload)
    
    for key, value in data.items():
        print(f"{key}: {value}")

        if key == "Bodenfeucht":
            pass
        elif key == "Feuchwand":
            pass
        elif key == "Tempwand":
            pass
        elif key == "TempBoden":
            pass
        elif key == "LED":
            pass
        elif key == "Luefter":
            pass
        elif key == "Pumpe":
            pass
        elif key == "Heizung":
            pass

# For debugging
# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#    print(client, userdata, level, buf)
