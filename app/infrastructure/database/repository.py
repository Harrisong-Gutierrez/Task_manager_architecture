# app/infrastructure/database/repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import datetime
from app.infrastructure.database.models import TaskModel
from app.core.models import Task, Priority

class TaskRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_task(self, task: Task) -> bool:
        """Guarda una nueva tarea en la base de datos"""
        task_model = TaskModel(
            id=task.id,
            title=task.title,
            description=task.description,
            priority=task.priority.value,
            created_at=task.created_at,
            completed=task.completed,
            due_date=task.due_date,
            task_type=task.task_type
        )
        self.db.add(task_model)
        try:
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def get_task(self, task_id: str) -> Optional[Task]:
        """Obtiene una tarea por su ID"""
        task_model = self.db.query(TaskModel).filter_by(id=task_id).first()
        if task_model:
            return self._to_domain(task_model)
        return None

    def list_tasks(self, completed: Optional[bool] = None, 
                  sort_by: str = "priority") -> List[Task]:
        """Lista tareas con filtros opcionales"""
        query = self.db.query(TaskModel)
        
        if completed is not None:
            query = query.filter_by(completed=completed)
            
        if sort_by == "priority":
            query = query.order_by(desc(TaskModel.priority), TaskModel.created_at)
        else:
            query = query.order_by(TaskModel.created_at)
            
        return [self._to_domain(task) for task in query.all()]

    def update_task(self, task: Task) -> bool:
        """Actualiza una tarea existente"""
        task_model = self.db.query(TaskModel).filter_by(id=task.id).first()
        if not task_model:
            return False
            
        task_model.title = task.title
        task_model.description = task.description
        task_model.priority = task.priority.value
        task_model.completed = task.completed
        task_model.due_date = task.due_date
        task_model.task_type = task.task_type
        
        try:
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def delete_task(self, task_id: str) -> bool:
        """Elimina una tarea"""
        task = self.db.query(TaskModel).filter_by(id=task_id).first()
        if not task:
            return False
            
        try:
            self.db.delete(task)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def _to_domain(self, task_model: TaskModel) -> Task:
        """Convierte el modelo de base de datos a dominio"""
        return Task(
            id=task_model.id,
            title=task_model.title,
            description=task_model.description,
            priority=Priority(task_model.priority),
            created_at=task_model.created_at,
            completed=task_model.completed,
            due_date=task_model.due_date,
            task_type=task_model.task_type
        )