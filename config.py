# config.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# Carga variables de entorno
load_dotenv()

class Config:
    """Configuración principal de la aplicación"""
    
    # Configuración de Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    
    # Configuración de Base de Datos
    DB_CONFIG = {
        'user': os.getenv('user'),
        'password': os.getenv('password'),
        'host': os.getenv('host'),
        'port': os.getenv('port'),
        'dbname': os.getenv('dbname')
    }
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración para testing (opcional)
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Engine para conexiones directas (opcional)
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    poolclass=NullPool,
    echo=False  # Cambiar a True para ver queries SQL en consola
)