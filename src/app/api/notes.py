from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import NoteDB, NoteSchema


router = APIRouter()


@router.post('/', response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    """router for create one note
      - Payload: NoteSchema
        - example: {"title": "123", "description": "456"}
      - Manual testing route: 
        - http --json POST http://localhost:8002/notes/ title=foo description=bar
    """
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.get("/{id}/", response_model=NoteDB)
async def read_note(id: int):
    """route for read single note
      - Path parameter:
        - id: id number for the note
    """
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/", response_model=List[NoteDB])
async def read_all_note():
    """route for read all notes"""
    return await crud.get_all()
