from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependency import get_post_service
from app.posts.extension import PostNotFoundException
from app.posts.schema import PostSchema
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
