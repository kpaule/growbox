from datetime import datetime

from flask_login import UserMixin

from growbox import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.password}')"


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(user_id)


class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    temperature_air = db.Column(db.Float, nullable=False)
    temperature_ground = db.Column(db.Float, nullable=False)
    humidity_air = db.Column(db.Float, nullable=False)
    humidity_ground = db.Column(db.Float, nullable=False)
    light = db.Column(db.Boolean, nullable=False)
    pump = db.Column(db.Boolean, nullable=False)
    heating = db.Column(db.Boolean, nullable=False)
    fan = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"Metric('{self.date}', '{self.temperature_air}', '{self.temperature_air}', '{self.temperature_ground}', '{self.humidity_wall}', '{self.light}', '{self.pump}', '{self.heating}', '{self.fan}')"
