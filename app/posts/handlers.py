from typing import Annotated, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Form,
    UploadFile,
    File, Query
)

from app.posts.posts_dependency import get_post_service
from app.posts.extension import PostNotFoundException
from app.posts.schema import PostSchema, PostCreateSchema
from app.posts.service import PostsService

router = APIRouter(prefix='/api/v1/memes', tags=['/api/v1/memes'])


@router.get(
    '',
    response_model=tuple[list[PostSchema], int]
)
async def get_posts(
        post_service: Annotated[PostsService, Depends(get_post_service)],
        page: int = Query(1, ge=1),
        page_size: int = Query(5, ge=1)
):
    posts, total_count_posts = await post_service.get_posts(
        page=page,
        page_size=page_size
    )
    return posts, total_count_posts


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
    try:
        return await post_service.delete_post(post_id=post_id)
    except PostNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )


@router.post(
    '',
    response_model=PostSchema,
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

    return await post_service.create_post(post=post)


@router.put(
    '/{post_id}',
    response_model=PostSchema
)
async def update_post(
        post_service: Annotated[PostsService, Depends(get_post_service)],
        post_id: int,
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

    body = PostCreateSchema(text=text, image_url=image_url)
    try:
        return await post_service.update_post(post_id=post_id, body=body)
    except PostNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
