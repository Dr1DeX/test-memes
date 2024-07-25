import pytest

from app.posts.post_settings import Settings


@pytest.fixture
def settings():
    return Settings()