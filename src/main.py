from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    task_id: int
    title: str
    description: str | None = None
    user_id: int
    working_on: bool = True
    finished: bool = False
    created_at: datetime | None = datetime.now()
    deadline: datetime

class User(BaseModel):
    user_id: int
    username: str
    password: str

app = FastAPI()


@app.put("/users/{user_id}")
async def create_task(user_id: int, new_task: Task):
    result = new_task.model_dump()
    result.update({"user_id": user_id})
    return result



@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item