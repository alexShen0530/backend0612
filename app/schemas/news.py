from email.policy import default

from pydantic import BaseModel, Field


class News(BaseModel):
    id:int
    title:str
    content:str = Field(default='')