from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255),comment='书名')
    author: Mapped[str] = mapped_column(String(255), comment='作者')
    price: Mapped[float] = mapped_column(Float, comment='价格')