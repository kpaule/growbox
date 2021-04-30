import random, time

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
    client.publish("growboxhsalbsensors/Bodenfeucht", random.uniform(1.5, 1.9), 0)
    client.publish("growboxhsalbsensors/Feuchwand", random.uniform(1.5, 1.9), 0)
    client.publish("growboxhsalbsensors/Tempwand", random.uniform(15.0, 16.0), 0)
    client.publish("growboxhsalbsensors/TempBoden", random.uniform(15.0, 16.0), 0)
    time.sleep(10)
