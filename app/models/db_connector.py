from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DatabaseAccessor:
    @classmethod
    def get_session(cls, config):
        mysql_url = config['SQLALCHEMY_DATABASE_URI']
        engine = create_engine(mysql_url)
        Base.metadata.bind = engine
        session = sessionmaker(bind=engine)
        session = session()
        return session

