# app/infrastructure/config.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# Carga variables de entorno
load_dotenv()

class Config:
    """Configuración de infraestructura para la aplicación"""
    
    # Configuración de base de datos
    DB_USER = os.getenv('user')
    DB_PASSWORD = os.getenv('password')
    DB_HOST = os.getenv('host')
    DB_PORT = os.getenv('port')
    DB_NAME = os.getenv('dbname')
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Engine para conexiones directas (opcional)
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    poolclass=NullPool,
    echo=False  # Cambiar a True para debug
)