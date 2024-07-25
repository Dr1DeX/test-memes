import pytest
from app.posts.schema import PostSchema, PostCreateSchema
from app.posts.service import PostsService

pytestmark = pytest.mark.asyncio


async def test_get_posts(posts_service: PostsService):
    page = 1
    page_size = 5
    posts, total_count = await posts_service.get_posts(page=page, page_size=page_size)

    assert len(posts) == page_size
    assert total_count == 10

    for post in posts:
        assert isinstance(post, PostSchema)
        assert post.image_url.startswith('fake')


async def test_get_post(posts_service: PostsService):
    post_id = 1

    post = await posts_service.get_post(post_id=post_id)

    assert post.id == post_id
    assert isinstance(post, PostSchema)
    assert isinstance(post.image_url, str)


async def test_create_post(posts_service: PostsService):
    post_create_data = PostCreateSchema(text='sample text', image_url=f'image_sample.jpg')

    created_post = await posts_service.create_post(post=post_create_data)

    assert isinstance(created_post, PostSchema)
    assert created_post.text == post_create_data.text
    assert created_post.image_url == post_create_data.image_url
