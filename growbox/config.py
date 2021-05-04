import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "key_for_development")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MQTT_BROKER_URL = "broker.hivemq.com"
    MQTT_BROKER_PORT = 1883
    MQTT_KEEPALIVE = 60
    MQTT_TLS_ENABLED = False
    MQTT_TOPIC = "growboxhsalbsensors"
    MQTT_TOPIC_CTRL = "growboxhsalb"