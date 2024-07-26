import asyncio
import json
import os

from app.posts.infrastructure.database.accessor import AsyncFactorySession
from app.posts.models import Posts
from app.posts.schema import PostCreateSchema
from app.s3.infrastructure import get_s3_client
from app.s3.s3_settings import settings
from sqlalchemy import insert

s3_client = get_s3_client()

image_dir = 'images'


def load_images():
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as data:
                    s3_client.put_object(
                        bucket_name=settings.MINIO_BUCKET_NAME,
                        object_name=file,
                        data=data,
                        length=-1,
                        part_size=10 * 1024 * 1024
                    )


async def load_data():
    with open('test_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    posts = [PostCreateSchema(**item) for item in data]
    async with AsyncFactorySession() as session:
        for post in posts:
            query = insert(Posts).values(**post.dict(exclude_none=True))
            await session.execute(query)
            await session.commit()
    load_images()


if __name__ == '__main__':
    asyncio.run(load_data())
