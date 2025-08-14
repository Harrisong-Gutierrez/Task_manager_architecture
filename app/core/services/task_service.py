from typing import Optional, List
from datetime import datetime
from uuid import uuid4
from ..models.task_models import Task, Priority
from app.infrastructure.database.repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(
        self,
        title: str,
        description: str,
        priority: Priority = Priority.MEDIUM,
        due_date: Optional[datetime] = None
    ) -> Task:
        """Crea una nueva tarea con validación de negocio"""
        if len(title) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres")
        if len(description) < 5:
            raise ValueError("La descripción debe tener al menos 5 caracteres")

        task = Task(
            id=str(uuid4()),
            title=title,
            description=description,
            priority=priority,
            created_at=datetime.utcnow(),
            due_date=due_date
        )

        if not self.repository.add_task(task):
            raise RuntimeError("Error al guardar la tarea en la base de datos")

        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        """Obtiene una tarea por su ID"""
        return self.repository.get_task(task_id)

    def list_tasks(
        self,
        completed: Optional[bool] = None,
        sort_by: str = "priority"
    ) -> List[Task]:
        """Lista tareas con filtros y ordenamiento"""
        valid_sort_fields = ["priority", "created_at"]
        if sort_by not in valid_sort_fields:
            sort_by = "priority"

        return self.repository.list_tasks(completed=completed, sort_by=sort_by)

    def complete_task(self, task_id: str) -> bool:
        """Marca una tarea como completada"""
        task = self.repository.get_task(task_id)
        if not task:
            return False

        task.completed = True
        return self.repository.update_task(task)

    def delete_task(self, task_id: str) -> bool:
        """Elimina una tarea"""
        return self.repository.delete_task(task_id)