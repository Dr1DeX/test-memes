from dataclasses import dataclass

import pytest

from app.posts.models import Posts
from app.posts.schema import PostCreateSchema
from tests.fixtures.posts.posts_model import FakePostsFactory


@dataclass
class FakePostsRepository:
    async def create_post(self, post: PostCreateSchema) -> int:
        new_post = FakePostsFactory(id=1, text=post.text, image_url=post.image_url)
        return new_post.id

    async def get_post(self, post_id: int) -> Posts:
        return FakePostsFactory.build(id=post_id, text='sample text', image_url='image_sample.jpg')

    async def get_posts(self) -> list[Posts]:
        return [
            FakePostsFactory.build()
            for _ in range(10)
        ]


@pytest.fixture
def posts_repository():
    return FakePostsRepository()
