from datetime import timedelta
import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    # API configurations
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY') or 'your-openweather-api-key'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') or 'your-news-api-key'
    
    # Cache configuration
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 3600  # 1 hour
    
    # API update intervals
    WEATHER_UPDATE_INTERVAL = timedelta(minutes=30)
    AIR_QUALITY_UPDATE_INTERVAL = timedelta(hours=1)
    NEWS_UPDATE_INTERVAL = timedelta(hours=2)
    
    # Default location (Paris)
    DEFAULT_LATITUDE = 48.8566
    DEFAULT_LONGITUDE = 2.3522