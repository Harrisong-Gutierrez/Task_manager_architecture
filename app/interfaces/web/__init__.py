# app/interfaces/web/__init__.py
from flask import Flask
from .routes import init_routes

def init_web_interface(app: Flask):
    """Inicializa todos los componentes web de la aplicación"""
    
    # Inicializa rutas/blueprints
    init_routes(app)
    
    # Registra templates y static files (automático en Flask)