from sqlalchemy import (
    Column,
    Table,
    Integer,
    Text,
    Numeric,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base

product_unit = Table('Product_Unit', Base.metadata,
                     Column('product_id', Integer, ForeignKey('Product.product_id')),
                     Column('unit_id', Integer, ForeignKey('Unit.unit_id'))
                     )


class Product(Base):
    __tablename__ = 'Product'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    retail_price = Column(Numeric(12, 2), nullable=False)
    wholesale_price = Column(Numeric(12, 2), nullable=False)
    description = Column(Text, nullable=False)
    discount_id = Column(Integer, ForeignKey('Discount.discount_id'), nullable=False)
    category_id = Column(Integer, ForeignKey('Category.category_id'), nullable=False)
    group_id = Column(Integer, ForeignKey('Group.group_id'), nullable=False)
    type_id = Column(Integer, ForeignKey('Type.type_id'), nullable=False)
    firm_id = Column(Integer, ForeignKey('Firm.firm_id'), nullable=False)

    discount = relationship("Discount", backref="products")
    category = relationship("Category", backref="products")
    group = relationship("Group", backref="products")
    type = relationship("Type", backref="products")
    firm = relationship("Firm", backref="products")

    units = relationship("Unit",
                         secondary=product_unit,
                         backref="products")
