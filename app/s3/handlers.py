from typing import Annotated

from fastapi import APIRouter, Depends

from app.s3.s3_dependency import get_s3_service
from app.s3.service import S3Service

router = APIRouter()


@router.get(
    '/files/{filename}'
)
def get_image(
        s3_service: Annotated[S3Service, Depends(get_s3_service)],
        filename: str
):
    return s3_service.get_image_url(file_name=filename)
