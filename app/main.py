import asyncio
from fastapi import FastAPI, Path, Query
import time
from app.schemas.Users import Users

app = FastAPI(
    title="backend test",
    description="web应用开发",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/sync")
def func_sync():
    start_time = time.time()
    for i in range(10):
        time.sleep(1)
    end = time.time()
    return {"time": f"{end - start_time:.2f}s"}

@app.get("/async")
async def func_async():
    start_time = time.time()
    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"time": f"{end - start_time:.2f}s"}

@app.get("/book/{id}")
async def get_book(id: str = Path(min_length=3,description="书籍id")):
    return {"id": f'你需要拿到id为{id}的书么'}

@app.get("/news/news_list")
async def get_news_list(
        skip: int = Query(description='skip跳过多少', gt=10),
        limit: int=Query(10, description='limit限制多少', lt=100)
):
    return {"skip": skip, "limit": limit}


@app.post("/user")
async def get_user_info(
        user: Users
):
    return {"name": user.username, "password": user.password}



