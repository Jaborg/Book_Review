from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI


application = FastAPI()
application.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@application.get("/")
async def index(request: Request):
    return templates.TemplateResponse("frontpage.html", {"request": request})


@application.get("/information")
async def info(request: Request):
    return templates.TemplateResponse("information.html", {"request": request})


@application.get("/reviews")
async def review(request: Request):

    return templates.TemplateResponse(
        "reviews.html", {"request": request}
    )


@application.get("/articles/")
def read_articles(request: Request):
    return templates.TemplateResponse(
        "reviews.html", {"request": request}
    )

@application.get("/articles/{id}")
def read_article_by_id(request: Request):
    return templates.TemplateResponse(
        "article.html", {"request": request}
    )