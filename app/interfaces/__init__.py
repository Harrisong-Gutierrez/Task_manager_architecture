# app/interfaces/__init__.py
# Exporta los módulos principales de interfaces

from .web import init_web_interface  # Importa la interfaz web

__all__ = [
    'init_web_interface'  # Exporta la función de inicialización
]