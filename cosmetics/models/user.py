import bcrypt
from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid_sacrud import PYRAMID_SACRUD_VIEW
from sqlalchemy import (
    Column,
    Integer,
    Text
)

from .meta import Base


class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    group = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    telephone = Column(Text)
    email = Column(Text)
    vk = Column(Text)

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False

    def __repr__(self):
        return "<User(%r)>" % self.name
