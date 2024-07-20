from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_ACCESS_KEY: str = "root"
    MINIO_SECRET_KEY: str = "password"
    MINIO_ENDPOINT: str = "minio:9090"
    MINIO_SECURE: bool = False
    MINIO_BUCKET_NAME: str = "minio-bucket"


settings = Settings()
