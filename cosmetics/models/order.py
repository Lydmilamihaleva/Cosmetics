from sqlalchemy import (
    Column,
    Integer,
    Date,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import relationship

from .meta import Base


class Order(Base):
    __tablename__ = 'Order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    date = Column(Date, nullable=False)
    total_price = Column(Numeric(12, 2), nullable=False)

    user = relationship("User", backref="orders")

