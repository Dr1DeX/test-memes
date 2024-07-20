from fastapi import Depends
from minio import Minio

from app.s3.infrastructure import get_s3_client
from app.s3.repository import S3Repository
from app.s3.service import S3Service


async def get_s3_repository(
        s3_client: Minio = Depends(get_s3_client)
) -> S3Repository:
    return S3Repository(s3_client=s3_client)


async def get_s3_service(
        s3_repository: S3Repository = Depends(get_s3_repository)
) -> S3Service:
    return S3Service(s3_repository=s3_repository)
