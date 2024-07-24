from typing import Optional

from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    text: str
    image_url: Optional[str] = None

    class Config:
        from_attributes = True


class PostCreateSchema(BaseModel):
    text: str
    image_url: Optional[str] = None
