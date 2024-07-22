from fastapi import FastAPI
from app.s3.handlers import router as s3_router


app = FastAPI(title='S3 service')
app.include_router(s3_router)
