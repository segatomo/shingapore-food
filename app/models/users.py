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
            'name': self.instance_id
        }
