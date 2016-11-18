from sqlalchemy import (
    Column,
    Integer
)

from .meta import Base


class Discount(Base):
    __tablename__ = 'Discount'

    discount_id = Column(Integer, primary_key=True, autoincrement=True)
    discount = Column(Integer, nullable=False)

