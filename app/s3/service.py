from dataclasses import dataclass

from app.s3.repository import S3Repository


@dataclass
class S3Service:
    s3_repository: S3Repository

    def upload_image(self, file_name: str, file_data: bytes, content_type: str) -> dict:
        return self.s3_repository.upload_image(
            file_name=file_name,
            file_data=file_data,
            content_type=content_type
        )

    def get_image_url(self, file_name: str) -> dict:
        return self.s3_repository.get_image_url(file_name=file_name)

    def delete_image(self, file_name: str) -> None:
        self.s3_repository.delete_image(file_name=file_name)
