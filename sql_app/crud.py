from sqlalchemy.orm import Session

from . import models, schemas


def get_article_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()



def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()




def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(id=article.id,title_art=article.title_art,picture = article.picture,
                                            date=article.date,main_text=article.main_text)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
