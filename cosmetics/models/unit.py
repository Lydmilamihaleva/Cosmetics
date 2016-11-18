from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class Unit(Base):
    __tablename__ = 'Unit'

    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

    def __repr__(self):
        return "<Unit(%r)>" % self.name
