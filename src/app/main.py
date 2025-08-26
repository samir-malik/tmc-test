from fastapi import FastAPI, Path, Request
from fastapi.responses import HTMLResponse
from starlette import status
from src.models.models_pydantic import UserCreatePayload
from src import utils
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
utils.create_db()
templates = Jinja2Templates(directory="src/templates/")
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request):
    return templates.TemplateResponse("index.html",  {"request": request})

@app.get("/create/user", response_class=HTMLResponse)
async def get_create_user_page(request: Request):
    return templates.TemplateResponse("create_user.html",  {"request": request})

@app.get("/users/list", response_class=HTMLResponse)
async def get_users_page(request: Request):
    return templates.TemplateResponse(
        "user_list.html", {"request": request,}
    )

@app.post("/users/create/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreatePayload):
    new_user = utils.create_user(payload)
    return new_user

#
@app.get("/users/", status_code=status.HTTP_200_OK)
async def get_users():
    return utils.get_users()

@app.delete("/user/{user_id}/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int = Path(gt=0)):
    utils.delete_user(user_id)
