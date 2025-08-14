# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.infrastructure.config import Config

# Inicializa extensiones
db = SQLAlchemy()

def create_app(config_class=Config):
    """Factory principal de la aplicación Flask"""
    
    # Configura la aplicación
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializa la base de datos
    db.init_app(app)
    
    # Configura la interfaz web
    from app.interfaces.web import init_web_interface
    init_web_interface(app)
    
    # Crea tablas si no existen (solo para desarrollo)
    with app.app_context():
        db.create_all()
    
    return app