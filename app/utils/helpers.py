# app/utils/helpers.py
from flask import flash
from datetime import datetime
from typing import Tuple, List, Optional

def validate_task_form(
    title: str, 
    description: str, 
    priority_str: str,
    due_date_str: Optional[str] = None
) -> Tuple[List[str], int, Optional[datetime]]:
    """
    Valida los datos del formulario de tareas.
    
    Returns:
        Tuple[List[str], int, Optional[datetime]]: 
        - Lista de errores
        - Prioridad como entero
        - Fecha límite como datetime (si aplica)
    """
    errors = []
    priority = 2  # Valor por defecto (Media)
    due_date = None

    # Validación de título
    if not title or len(title.strip()) < 3:
        errors.append("El título debe tener al menos 3 caracteres")

    # Validación de descripción
    if not description or len(description.strip()) < 5:
        errors.append("La descripción debe tener al menos 5 caracteres")

    # Validación de prioridad
    try:
        priority = int(priority_str)
        if priority not in [1, 2, 3]:
            errors.append("Prioridad inválida (debe ser 1, 2 o 3)")
    except (ValueError, TypeError):
        errors.append("La prioridad debe ser un número válido")

    # Validación de fecha
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            errors.append("Formato de fecha inválido. Use YYYY-MM-DD")

    return errors, priority, due_date


def flash_errors(errors: List[str]) -> None:
    """Muestra errores como mensajes flash"""
    for error in errors:
        flash(error, "danger")