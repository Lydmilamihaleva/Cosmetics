from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base


class Picture(Base):
    __tablename__ = 'Picture'

    picture_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('Product.product_id'))
    link = Column(Text, nullable=False)

    product = relationship("Product", backref="pictures")
