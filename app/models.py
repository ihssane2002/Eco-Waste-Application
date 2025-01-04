from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telephone = db.Column(db.String(20))
    password = db.Column(db.String(60), nullable=False)
    points = db.Column(db.Integer, default=0)
    organic_waste = db.Column(db.Float, default=0)
    inorganic_waste = db.Column(db.Float, default=0)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class CollectionPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    horaire = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    type_dechet = db.Column(db.String(50))
    date_collecte = db.Column(db.DateTime)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(200))
    source = db.Column(db.String(200))
    auteur = db.Column(db.String(100))

class EnvironmentalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    weather_description = db.Column(db.String(100))
    weather_icon = db.Column(db.String(10))
    air_quality_index = db.Column(db.Integer)
    pm25_level = db.Column(db.Float)
    pm10_level = db.Column(db.Float)
    no2_level = db.Column(db.Float)
    is_collection_favorable = db.Column(db.Boolean, default=True)

class EnvironmentalNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class hi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)