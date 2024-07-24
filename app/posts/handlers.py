from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile, File

from app.posts.posts_dependency import get_post_service
from app.posts.extension import PostNotFoundException
from app.posts.schema import PostSchema, PostCreateSchema
from app.posts.service import PostsService

router = APIRouter(prefix='/memes', tags=['memes'])


@router.get(
    '',
    response_model=list[PostSchema]
)
async def get_posts(
        post_service: Annotated[PostsService, Depends(get_post_service)]
):
    return await post_service.get_posts()


@router.get(
    '/{post_id}',
    response_model=PostSchema
)
async def get_post(
        post_service: Annotated[PostsService, Depends(get_post_service)],
        post_id: int
):
    try:
        return await post_service.get_post(post_id=post_id)
    except PostNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )


@router.delete(
    '/{post_id}'
)
async def delete_post(
        post_service: Annotated[PostsService, Depends(get_post_service)],
        post_id: int
):
    return await post_service.delete_post(post_id=post_id)


@router.post(
    '',
    response_model=PostSchema
)
async def create_post(
        post_service: Annotated[PostsService, Depends(get_post_service)],
        text: Annotated[str, Form(...)],
        image: Optional[UploadFile] = File(None)
):
    if image:
        image_data = await image.read()
        image_url = post_service.upload_image(
            file_name=image.filename,
            file_data=image_data,
            content_type=image.content_type
        )
    else:
        image_url = None

    post = PostCreateSchema(text=text, image_url=image_url)
    print(post)

    return await post_service.create_post(post=post)