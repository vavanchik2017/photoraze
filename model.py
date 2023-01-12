from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import create_engine, delete, update
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///photoraze.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name, tags):
        img = cls(name=name, tags=tags)
        session.add(img)
        session.commit()
        return img

    @classmethod
    def delete(cls, id):
        delpic = session.query(cls).filter(cls.__table__.c.id == id).one()
        session.delete(delpic)
        session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_tags(cls, id: int):
        q=session.query(cls).filter_by(id=id).first()
        print (q.tags)
        return str(q)

    @classmethod
    def get_image_byid(cls, id):
        return session.query(cls).filter(cls.id == id)

    @classmethod
    def get_image_bytag(cls, tag):
        search_request = "%{}%".format(tag)
        return session.query(cls).filter(cls.tags.like(search_request))

    @classmethod
    def update_name(cls, id, name):
        stmt = (
            update(cls.__table__).
            where(cls.__table__.c.id == id).
            values(name=name)
        )
        session.execute(stmt)
        session.commit()

    @classmethod
    def update_tags(cls, id: int, tags: str):
        stmt = (
            update(cls.__table__).
            where(cls.__table__.c.id == id).
            values(tags=tags)
        )
        session.execute(stmt)
        session.commit()


Base.metadata.create_all(engine)
