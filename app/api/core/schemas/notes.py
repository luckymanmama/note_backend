from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    body: str
    user_id: int


class NoteUpdate(NoteCreate):
    pass
