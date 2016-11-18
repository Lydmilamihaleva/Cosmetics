from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Storage(Base):
    __tablename__ = 'Storage'

    product_id = Column(Integer, ForeignKey('Product.product_id'), primary_key=True, unique=True)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", backref=backref("storage", uselist=False))
