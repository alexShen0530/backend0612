from pydantic import BaseModel, Field
from fastapi import Query

class Users(BaseModel):
    username: str = Field(..., min_length=3, max_length=10, description="用户名")
    password: str
    email: str = Field(default='', description="邮箱")

    爱你
