from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.authentication import current_active_user
from ..core.crud import CRUDBase
from ..core.models.notes import Note
from ..core.models.users import User
from ..core.schemas.notes import NoteCreate, NoteUpdate
from ..core.session import get_db
from ..core.utils import check_note_ownership

router = APIRouter()
notes_crud = CRUDBase(Note)


@router.get("/")
@check_note_ownership
async def get_all_notes(db: AsyncSession = Depends(get_db)):
    return await notes_crud.get_all(db)


@router.get("/{id}")
@check_note_ownership
async def get_note(id: int, db: AsyncSession = Depends(get_db)):
    note = await notes_crud.get(db, id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("/")
async def create_note(note_in: NoteCreate,
                      db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(current_active_user),
                      ):
    return await notes_crud.create(db, obj_in={**note_in, "user_id": current_user.id})


@router.put("/{id}")
@check_note_ownership
async def update_note(id: int, note_in: NoteUpdate, db: AsyncSession = Depends(get_db)):
    note = await notes_crud.get(db, id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return await notes_crud.update(db, db_obj=note, obj_in=note_in)


@router.delete("/{id}")
@check_note_ownership
async def delete_note(id: int, db: AsyncSession = Depends(get_db)):
    note = await notes_crud.get(db, id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return await notes_crud.delete(db, db_obj=note)
