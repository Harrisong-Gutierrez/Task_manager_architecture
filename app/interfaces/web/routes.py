# app/interfaces/web/routes.py
from flask import Blueprint
from .controllers.task_controller import bp as task_bp

def init_routes(app):
    """Registra todos los blueprints de la interfaz web"""
    
    # Registra el blueprint de tareas
    app.register_blueprint(task_bp)
    
    # Puedes agregar más blueprints aquí:
    # app.register_blueprint(otro_bp)
    # app.register_blueprint(otro_mas_bp)