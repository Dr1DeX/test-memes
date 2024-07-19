from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True


class PostCreateSchema(BaseModel):
    title: str
    description: str
