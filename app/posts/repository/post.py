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
            query: Sequence[Posts] = (await session.execute(select(Posts))).scalars().all()
            return query
