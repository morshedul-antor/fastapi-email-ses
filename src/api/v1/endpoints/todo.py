from fastapi import APIRouter, Depends, HTTPException
from schemas import TodoIn, TodoOut, TodoUpdate
from exceptions.service_result import handle_result
from sqlalchemy.orm import Session
from db import get_db
from typing import List
from services import todo_service
import boto3

router = APIRouter()


@router.get('/', response_model=List[TodoOut])
def all_todo(skip: int = 0, limit: int = 10,  db: Session = Depends(get_db)):
    all = todo_service.get_with_pagination(
        db=db, skip=skip, limit=limit, descending=True)
    return handle_result(all)


@router.post('/', response_model=TodoOut)
def create_todo(data_in: TodoIn, db: Session = Depends(get_db)):
    todo = todo_service.create_todo(db=db, data_in=data_in)
    return handle_result(todo)


@router.put('/{id}', response_model=TodoOut)
def update_todo(id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    update = todo_service.update(db, id, data_update=todo_update)
    return handle_result(update)


@router.delete('/{id}')
def delete_todo(id: int, db: Session = Depends(get_db)):
    delete = todo_service.delete(db, id=id)
    return handle_result(delete)
