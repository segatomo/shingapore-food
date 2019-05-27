from sqlalchemy import Column,  String, DateTime, Integer, FetchedValue
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, nullable=False, primary_key=True)
    name = Column("name", String(255), nullable=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Users1(Base):
    __tablename__ = 'users1'

    password = Column("id", Integer, nullable=False, primary_key=True)
    username = Column("name", String(255), nullable=True)
    picturepath = Column("picname",String(255),nullable=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
