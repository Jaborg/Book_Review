from sqlalchemy.orm import Session

from . import models, schemas


def get_article_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()





def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(title=article.title)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_article
