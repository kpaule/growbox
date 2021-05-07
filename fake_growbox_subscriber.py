import paho.mqtt.client as paho


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("growboxhsalb/#")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
