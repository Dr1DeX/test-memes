from dataclasses import dataclass

import pytest


@dataclass
class FakeS3Repository:

    def get_image_url(self, file_name: str) -> dict:
        return {'image_url': 'fake'}


@pytest.fixture
def s3_repository():
    return FakeS3Repository()
