import asyncio
from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, FileResponse
import time
from app.schemas.users import Users
from app.schemas.news import News

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
@app.get("/news/{id}", response_model=News)
async def get_news(
        id:int = Path(...,gt=2)
):
    return {
        'id':id,
        'title':'alex'
    }





