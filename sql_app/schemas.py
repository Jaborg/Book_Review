from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    description: Optional[str] = None


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
