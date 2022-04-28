from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    id: int


class ArticleCreate(ArticleBase):
    title_art: str
    picture:str
    date:str



class Article(ArticleBase):
    is_reviewed: bool
    title_art: str
    picture:str


    class Config:
        orm_mode = True
