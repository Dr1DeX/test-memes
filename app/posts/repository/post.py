from dataclasses import dataclass
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.posts.models import Posts


@dataclass
class PostsRepository:
    db_session: AsyncSession

    async def get_posts(self) -> Sequence[Posts]:

        async with self.db_session as session:
            posts: Sequence[Posts] = (await session.execute(select(Posts))).scalars().all()
            return posts

    async def get_post(self, post_id: int) -> Posts:
        query = select(Posts).where(Posts.id == post_id)

        async with self.db_session as session:
            post: Posts = (await session.execute(query)).scalar_one_or_none()
            return post
