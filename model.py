from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///photoraze.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Image(Base):
    __tablename__ = "images"
    id=Column(Integer,primary_key=True)
    name = Column(String)
    tags = Column(String)

    def __str__(self):
        return self.name
    @classmethod
    def add(cls,name,tags):
        img = cls(name=name,tags=tags)
        session.add(img)
        session.commit()
        return img
    @classmethod
    def get_all(cls):
        session.query(cls).all()