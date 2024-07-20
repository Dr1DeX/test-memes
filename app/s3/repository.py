import io

from minio import Minio
from dataclasses import dataclass

from app.s3.s3_settings import settings


@dataclass
class S3Repository:
    s3_client: Minio

    async def upload_image(self, file_name: str, file_data: bytes, content_type: str) -> str:
        self.s3_client.put_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=file_name,
            data=io.BytesIO(file_data),
            length=len(file_data),
            content_type=content_type
        )
        return self.get_image_url(file_name=file_name)

    def get_image_url(self, file_name: str) -> str:
        return self.s3_client.presigned_get_object(bucket_name=settings.MINIO_BUCKET_NAME, object_name=file_name)
