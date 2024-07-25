import io

from minio import Minio
from dataclasses import dataclass

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
        nginx_url = f'/{settings.MINIO_BUCKET_NAME}/{file_name}'
        return self.get_image_url(file_name=nginx_url)

    def get_image_url(self, file_name: str) -> dict:

        return {'image_url': file_name}

    def delete_image(self, file_name: str) -> None:
        slicer_name = file_name.split('/')[-1]
        self.s3_client.remove_object(bucket_name=settings.MINIO_BUCKET_NAME, object_name=slicer_name)
