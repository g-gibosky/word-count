from fastapi import FastAPI
from .application.mainService import mainService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_main():
    return {"msg": "Seja bem vindo(a) ao teste da VOXY de Guilherme Gibosky"}


@app.post("/api/word-count/")
def word_count(form_info: dict):
    main_service = mainService()
    return main_service.count_words(form_info)