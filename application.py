from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

application = FastAPI()
application.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@application.get("/")
async def index(request: Request):
    return templates.TemplateResponse("frontpage.html", {"request": request})


@application.get("/information")
async def info(request: Request):
    return templates.TemplateResponse("information.html", {"request": request})


@application.get("/reviews")
async def review(request: Request, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=0, limit=100)

    return templates.TemplateResponse(
        "reviews.html", {"request": request, "articles": articles}
    )


@application.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud.get_article_by_id(db, article_id=article.id)
    if db_article:
        raise HTTPException(status_code=400, detail="ID already posted")
    return crud.create_article(db=db, article=article)


@application.get("/articles/", response_model=list[schemas.Article])
def read_articles(
    request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return templates.TemplateResponse(
        "reviews.html", {"request": request, "articles": articles}
    )


@application.get("/articles/{id}", response_model=schemas.Article)
def read_article_by_id(request: Request, id=id, db: Session = Depends(get_db)):
    article = crud.get_article_by_id(db, id)
    return templates.TemplateResponse(
        "article.html", {"request": request, "article": article}
    )


#
#
#
# Response body
# Download
# [
#   {
#     "id": 1,
#     "is_reviewed": false,
#     "title_art": "emma",
#     "picture": "something.url"
#   },
#   {
#     "id": 2,
#     "is_reviewed": false,
#     "title_art": "moon",
#     "picture": "something_else.url"
#   }
# ]
