import asyncio
from fastapi import FastAPI, Path, Query, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, FileResponse
import time

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import Users
from app.schemas.news import News
from app.dependencies import common_params
from app.database import Base, async_engine, get_db
from app.models.book import Book
from typing import Optional

app = FastAPI(
    title="backend test",
    description="web应用开发",
    version="1.0.0"
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    body = await request.body()
    print(body.decode("utf-8"))
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} completed in {process_time}s")
    return response

# @app.middleware("http")
# async def log_requests1(request: Request, call_next):
#     print('1st middleware')
#     response = await call_next(request)
#     print(f"你好")
#     return response

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str):
    return ['hello world']

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
async def get_book(id: int = Path(..., gt=0, lt=1000)):
    if id not in [1,2,3,4,5]:
        raise HTTPException(status_code=404, detail="你查找的图书id无效")
    return {"id": f'你需要拿到id为{id}的书么'}


@app.post("/user")
async def get_user_info(
        user: Users
):
    return {"name": user.username, "password": user.password}


# 装饰器的响应类
@app.get("/html/{name}", response_class=HTMLResponse)
async def get_html(name:str):
    return f"<h1>hello {name}</h1>"


# 返回响应对象
@app.get("/get_file")
async def get_file():
    file_path = r"C:\Users\Windows\Downloads\中国高等教育学位在线验证报告_申鑫.pdf"
    return FileResponse(file_path)

#自定义响应数据格式
@app.get("/{id}/news", response_model=News)
async def get_news(
        title:str,
        id:int = Path(...,gt=2)
):
    return {
        'id':id,
        'title':title
    }


@app.get("/news/news_list")
async def get_book_list(
        price:float,
        book_id:int|None = None,
        db:AsyncSession = Depends(get_db)
):
    # result = await db.execute(
    #     select(func.sum(Book.price))
    #       .where((Book.price >= price) & (Book.title.like('%python%')))
    # )
    result = await db.execute(
        select(Book).offset(2).limit(2)
    )
    # result = await db.get(Book, book_id)
    return {'books':result.scalars().all()}

@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




