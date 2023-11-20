from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    body: str


class NoteUpdate(NoteCreate):
    pass
