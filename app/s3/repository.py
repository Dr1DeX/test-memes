import io

from fastapi import HTTPException, status

from minio import Minio, S3Error
from dataclasses import dataclass
from urllib.parse import urlparse, urlunparse, ParseResult

from app.s3.s3_settings import settings


@dataclass
class S3Repository:
    s3_client: Minio

    def upload_image(self, file_name: str, file_data: bytes, content_type: str) -> dict:
        self.s3_client.put_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=file_name,
            data=io.BytesIO(file_data),
            length=len(file_data),
            content_type=content_type
        )
        return self.get_image_url(file_name=file_name)

    def get_image_url(self, file_name: str) -> dict:

        nginx_url = f'/{settings.MINIO_BUCKET_NAME}/{file_name}'

        return {'image_url': nginx_url}
