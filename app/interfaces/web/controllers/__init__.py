# app/interfaces/web/controllers/__init__.py
# Exporta los controladores disponibles para el módulo web

from .task_controller import bp as task_bp  # Importa el Blueprint de tareas

__all__ = [
    'task_bp'  # Exporta el Blueprint para su registro en la aplicación
]