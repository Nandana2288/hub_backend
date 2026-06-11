import uuid
from datetime import datetime

from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    title: str
    description: str | None = None
    due_date: datetime | None = None


class UpdateTodoRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None


class CompleteToggleRequest(BaseModel):
    completed: bool


class TodoResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None
    completed: bool
    due_date: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
