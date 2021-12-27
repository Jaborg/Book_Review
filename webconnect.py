from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="templates")



@app.get("/")
async def index(request : Request):


    return templates.TemplateResponse("frontpage.html",
        {"request":request })
