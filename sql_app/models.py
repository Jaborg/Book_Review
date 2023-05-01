from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title_art = Column(String)
    main_text = Column(String)
    picture = Column(String)
    is_reviewed = Column(Boolean, default=False)
    date = Column(String, default=False)
