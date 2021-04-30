import random, time, json

import paho.mqtt.client as paho


def handle_publish(client, userdata, mid):
    print(f"CLIENT {client} PUBLISHING mid: {mid}")


client = paho.Client(client_id="12")
client.on_publish = handle_publish
client.connect("broker.hivemq.com", 1883)
client.loop_start()

while True:
    #client.publish("growboxhsalb", "{\"LED\":\"off\"}")
    #client.publish("growboxhsalb", "{\"Pumpe\":\"off\"}")
    #client.publish("growboxhsalb", "{\"Heizung\":\"off\"}")
    #client.publish("growboxhsalb", "{\"Luefter\":\"off\"}")

    test_dict = {
        "Bodenfeucht": random.uniform(1.5, 1.9),
        "Feuchwand": random.uniform(1.5, 1.9),
        "Tempwand": random.uniform(15.0, 16.0),
        "TempBoden": random.uniform(15.0, 16.0)
    }

    client.publish("growboxhsalbsensors", json.dumps(test_dict), 0)
    time.sleep(10)
