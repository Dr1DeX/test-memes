from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependency import get_post_service
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
