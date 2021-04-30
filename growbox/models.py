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


class TemperatureWall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"TemperatureWall('{self.temperature}', '{self.date}')"


class TemperatureFloor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"TemperatureFloor('{self.temperature}', '{self.date}')"


class HumidityWall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"HumidityWall('{self.humidity}', '{self.date}')"


class HumidityFloor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"HumidityFloor('{self.humidity}', '{self.date}')"
