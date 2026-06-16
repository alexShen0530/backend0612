from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 创建异步引擎
aysnc_database_url = "mysql+aiomysql://root:7138598Sx%40@localhost:3306/fastapi_test?charset=utf8mb4"
async_engine = create_async_engine(aysnc_database_url, echo=True, pool_size=10, max_overflow=20)

# 基类
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, default=func.now(), comment='创建时间')
    update_time: Mapped[datetime] = mapped_column(DateTime, default=func.now(), comment='更新时间')

