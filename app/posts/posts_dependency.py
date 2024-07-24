from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.posts.infrastructure.database import get_db_session
from app.posts.post_settings import Settings
from app.posts.repository import PostsRepository
from app.posts.service import PostsService
from app.s3.repository import S3Repository
from app.s3.s3_dependency import get_s3_repository


async def get_post_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> PostsRepository:
    return PostsRepository(db_session=db_session)


async def get_post_service(
        post_repository: PostsRepository = Depends(get_post_repository),
        s3_repository: S3Repository = Depends(get_s3_repository)
) -> PostsService:
    return PostsService(
        post_repository=post_repository,
        settings=Settings(),
        s3_repository=s3_repository
    )
