from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import relationship

from .meta import Base


class OrderItem(Base):
    __tablename__ = 'Order_Item'

    product_id = Column(Integer, ForeignKey('Product.product_id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('Order.order_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)

    product = relationship("Product", backref="order_items")
    order = relationship("Order", backref="order_items")