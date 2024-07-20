from dataclasses import dataclass
from typing import Sequence

from app.posts.extension import PostNotFoundException
from app.posts.models import Posts
from app.posts.schema import PostSchema
from app.posts.repository import PostsRepository


@dataclass
class PostsService:
    post_repository: PostsRepository

    async def get_posts(self) -> list[PostSchema]:
        posts: Sequence[Posts] = await self.post_repository.get_posts()
        posts_schema: list[PostSchema] = [PostSchema.model_validate(post) for post in posts]
        return posts_schema

    async def get_post(self, post_id: int) -> PostSchema:
        post: Posts = await self.post_repository.get_post(post_id=post_id)

        if not post:
            raise PostNotFoundException

        post_schema = PostSchema.model_validate(post)
        return post_schema

    async def delete_post(self, post_id: int) -> str:
        await self.post_repository.delete_memes(post_id=post_id)
        message = f'Post id={post_id} delete success !'
        return message
