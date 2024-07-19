from fastapi import FastAPI

from app.posts.handlers import router as posts_router

app = FastAPI(title='Сервис со смешнявками :3')

app.include_router(posts_router)
