from dataclasses import dataclass

from app.posts.schema import PostSchema
from app.posts.repository import PostsRepository


@dataclass
class PostsService:
    post_repository: PostsRepository

    async def get_posts(self) -> list[PostSchema]:
        posts = await self.post_repository.get_posts()
        posts_schema = [PostSchema.model_validate(post) for post in posts]
        return posts_schema
