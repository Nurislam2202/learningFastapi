import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="Главная ручка", tags=["Основные ручки"])
def root():
    return "Hello World"


# books = [
#     {
#         "id": 1,
#         "title": "Асинхронность в Python",
#         "author": "Меттью",
#     },
#     {
#         "id": 2,
#         "title": "Backend разработка в Python",
#         "author": "Артем"
#     }
# ]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# запуск командой python main.py
