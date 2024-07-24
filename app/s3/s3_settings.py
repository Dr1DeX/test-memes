from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_SECURE: bool = False
    MINIO_BUCKET_NAME: str = "memes-images"


settings = Settings()
