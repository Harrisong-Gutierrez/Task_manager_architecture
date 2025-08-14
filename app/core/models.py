# app/core/models.py
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
    @property
    def name(self) -> str:
        names = {
            1: "Baja",
            2: "Media", 
            3: "Alta"
        }
        return names[self.value]

@dataclass
class Task:
    id: str
    title: str
    description: str
    priority: Priority
    created_at: datetime
    completed: bool = False
    due_date: Optional[datetime] = None
    task_type: str = "normal"