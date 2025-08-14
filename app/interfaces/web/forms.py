# app/interfaces/web/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Length
from app.core.models import Priority

class TaskForm(FlaskForm):
    """Formulario para creación/edición de tareas"""
    
    title = StringField(
        'Título',
        validators=[
            DataRequired(message="El título es obligatorio"),
            Length(min=3, max=100, message="El título debe tener entre 3 y 100 caracteres")
        ],
        render_kw={"placeholder": "Título de la tarea"}
    )
    
    description = TextAreaField(
        'Descripción',
        validators=[
            DataRequired(message="La descripción es obligatoria"),
            Length(min=5, max=255, message="La descripción debe tener entre 5 y 255 caracteres")
        ],
        render_kw={"placeholder": "Descripción detallada...", "rows": 3}
    )
    
    priority = SelectField(
        'Prioridad',
        choices=[
            (Priority.LOW.value, 'Baja'),
            (Priority.MEDIUM.value, 'Media'),
            (Priority.HIGH.value, 'Alta')
        ],
        coerce=int,
        default=Priority.MEDIUM.value
    )
    
    has_due_date = BooleanField(
        '¿Tiene fecha límite?',
        default=False
    )
    
    due_date = DateField(
        'Fecha Límite',
        format='%Y-%m-%d',
        validators=[],
        render_kw={"disabled": True}
    )