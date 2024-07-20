from minio import Minio

from app.s3.s3_settings import settings


def get_s3_client() -> Minio:
    s3_client = Minio(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=False
    )

    if not s3_client.bucket_exists(bucket_name=settings.MINIO_BUCKET_NAME):
        s3_client.make_bucket(bucket_name=settings.MINIO_BUCKET_NAME)

    return s3_client
