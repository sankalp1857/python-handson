from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/hello")
def read_item(name: str, info: Optional[str] = None):
    return {"Hello": name, "info": info}
