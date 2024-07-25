from dataclasses import dataclass

from app.posts.extension import PostNotFoundException
from app.posts.post_settings import Settings
from app.posts.schema import PostSchema, PostCreateSchema
from app.posts.repository import PostsRepository
from app.s3.repository import S3Repository


@dataclass
class PostsService:
    post_repository: PostsRepository
    s3_repository: S3Repository
    settings: Settings

    async def get_posts(
            self,
            page: int,
            page_size: int
    ) -> tuple[list[PostSchema], int]:
        posts = await self.post_repository.get_posts()
        posts_schema = [
            PostSchema(
                id=post.id,
                text=post.text,
                image_url=self._get_image_url(filename=post.image_url)
            )
            for post in posts
        ]
        total_count_posts = len(posts)
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return posts_schema[start_index:end_index], total_count_posts

    async def get_post(self, post_id: int) -> PostSchema:
        post = await self.post_repository.get_post(post_id=post_id)

        if not post:
            raise PostNotFoundException

        post_schema = PostSchema.model_validate(post)
        return post_schema

    async def delete_post(self, post_id: int) -> str:
        post = await self.post_repository.get_post(post_id=post_id)
        if not post:
            raise PostNotFoundException
        if post.image_url:
            self.s3_repository.delete_image(file_name=post.image_url)

        await self.post_repository.delete_memes(post_id=post_id)

        message = f'Post id={post_id} delete success !'
        return message

    def _get_image_url(self, filename: str):
        image_url: dict = self.s3_repository.get_image_url(
            file_name=filename
        )
        return image_url['image_url']

    def upload_image(
            self,
            file_name: str,
            file_data: bytes,
            content_type: str
    ) -> str:
        result = self.s3_repository.upload_image(
            file_name=file_name,
            file_data=file_data,
            content_type=content_type
        )
        return result['image_url']

    async def create_post(self, post: PostCreateSchema) -> PostSchema:
        post_id = await self.post_repository.create_post(post=post)
        post = await self.post_repository.get_post(post_id=post_id)
        return PostSchema.model_validate(post)

    async def update_post(
            self,
            post_id: int,
            body: PostCreateSchema
    ) -> PostSchema:
        await self.post_repository.update_post(post_id=post_id, body=body)
        updated_post = await self.post_repository.get_post(post_id=post_id)

        if not updated_post:
            raise PostNotFoundException
        return PostSchema.model_validate(updated_post)
