from dataclasses import dataclass
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, insert, update

from app.posts.models import Posts
from app.posts.schema import PostCreateSchema


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

    async def delete_memes(self, post_id: int) -> None:
        query = delete(Posts).where(Posts.id == post_id)

        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def create_post(self, post: PostCreateSchema) -> int:
        query = insert(Posts).values(**post.dict(exclude_none=True)).returning(Posts.id)

        async with self.db_session as session:
            post_id: int = (await session.execute(query)).scalar_one_or_none()
            await session.commit()
            return post_id

    async def update_post(self, post_id: int, body: PostCreateSchema) -> None:
        query = (
            update(Posts)
            .where(Posts.id == post_id)
            .values(**body.dict(exclude_none=True))
        )

        async with self.db_session as session:
            await session.execute(query)
            await session.commit()
