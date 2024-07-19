from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db_session
from app.posts.repository import PostsRepository
from app.posts.service import PostsService


async def get_post_repository(
        db_session: AsyncSession = Depends(get_db_session)
) -> PostsRepository:
    return PostsRepository(db_session=db_session)


async def get_post_service(
        post_repository: PostsRepository = Depends(get_post_repository)
) -> PostsService:
    return PostsService(post_repository=post_repository)
