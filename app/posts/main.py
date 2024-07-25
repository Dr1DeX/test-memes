from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.posts.handlers import router as posts_router

app = FastAPI(title='Сервис со смешнявками :3')

app.include_router(posts_router)


origins = [
    'http://localhost:3000',
    'http://localhost',
    'localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
