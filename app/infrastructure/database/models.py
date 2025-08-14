from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskModel(Base):
    """Modelo SQLAlchemy para la tabla tasks"""
    __tablename__ = 'tasks'

    id = Column(String(36), primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    priority = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
    due_date = Column(DateTime, nullable=True)
    task_type = Column(String(20), default='normal')