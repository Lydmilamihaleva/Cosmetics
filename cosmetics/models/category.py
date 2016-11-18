from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Category(Base):
    __tablename__ = 'Category'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
