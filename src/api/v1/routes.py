from fastapi import APIRouter

from .endpoints import todo, emails

api_router = APIRouter()

# fmt: off
# api_router.include_router(todo.router, prefix='/todo', tags=['Todos'])
api_router.include_router(emails.router, prefix='/ses', tags=['SES Emails'])