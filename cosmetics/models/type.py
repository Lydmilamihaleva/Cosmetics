from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class Type(Base):
    __tablename__ = 'Type'

    type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

    def __repr__(self):
        return "<Type(%r)>" % self.name
