from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Firm(Base):
    __tablename__ = 'Firm'

    firm_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return "<Firm(%r)>" % self.name
