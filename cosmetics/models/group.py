from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Group(Base):
    __tablename__ = 'Group'

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
