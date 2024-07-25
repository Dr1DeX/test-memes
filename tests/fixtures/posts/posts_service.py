from unittest.mock import MagicMock

import pytest

from app.posts.post_settings import settings
from app.posts.service import PostsService


@pytest.fixture
def posts_service(posts_repository, s3_repository):
    return PostsService(
        post_repository=posts_repository,
        s3_repository=s3_repository,
        settings=settings
    )
