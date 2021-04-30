from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from growbox.config import Config
from flask_mqtt import Mqtt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "info"
mqtt = Mqtt()
socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    from growbox.main.routes import main
    from growbox.home.routes import home
    app.register_blueprint(main)
    app.register_blueprint(home)

    from growbox.mqtt_client.subscriber import mqtt_client
    app.register_blueprint(mqtt_client)

    mqtt.init_app(app)

    return app