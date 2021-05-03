import json
import logging

from growbox import create_app, db, mqtt
from growbox.models import (HumidityFloor, HumidityWall, TemperatureFloor,
                            TemperatureWall)


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
    
    # outside an application context -> manually push a context
    with create_app().app_context():
        for key, value in data.items():
            # Validate mqtt data to prevent xss vulnerability
            if type(value) == float or value == "on" or value == "off":
                print(f"{key}: {value}")

                if key == "Bodenfeucht":
                    humidityFloor = HumidityFloor(humidity=value)
                    db.session.add(humidityFloor)
                elif key == "Feuchwand":
                    humidityWall = HumidityWall(humidity=value)
                    db.session.add(humidityWall)
                elif key == "Tempwand":
                    temperatureWall = TemperatureWall(temperature=value)
                    db.session.add(temperatureWall)
                elif key == "TempBoden":
                    temperatureFloor = TemperatureFloor(temperature=value)
                    db.session.add(temperatureFloor)
                elif key == "LED":
                    pass
                elif key == "Luefter":
                    pass
                elif key == "Pumpe":
                    pass
                elif key == "Heizung":
                    pass
            else:
                print(f"Unexpected mqtt data recived: ({key}: {value})")

        db.session.commit()

# For debugging
# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#    print(client, userdata, level, buf)
