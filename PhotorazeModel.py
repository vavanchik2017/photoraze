from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import create_engine, delete, update
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///photoraze.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class ImageModel(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(String)
    path = Column(String)

    def __str__(self):
        return self.name


class ImageFacade:
    def __init__(self):
        self.image = ImageModel

    def add(self, name, tags, path):
        img = self.image(name=name, tags=tags, path=path)
        session.add(img)
        session.commit()
        session.close()


    def delete(self, id):
        session = Session()
        delpic = session.query(self.image).filter(self.image.__table__.c.id == id).one()
        session.delete(delpic)
        session.commit()
        session.close()

    def get_all(self):
        t = session.query(self.image).all()
        session.close()
        return t

    def get_tags(self, id: int):
        session = Session()
        q = session.query(self.image).filter_by(id=id).first()
        session.close()
        return str(q)

    def get_image_byid(self, id):
        session = Session()
        resp=session.query(self.image).filter(self.image.id == id).first()
        session.close()
        return resp
    def get_image_bytag(self, tag):
        search_request = "%{}%".format(tag)
        session = Session()
        resp=session.query(self.image).filter(self.image.tags.like(search_request)).all()
        session.close()
        return resp
    def update_name(self, id, name):
        session = Session()
        stmt = (
            update(self.image.__table__).
            where(self.image.__table__.c.id == id).
            values(name=name)
        )
        session.execute(stmt)
        session.commit()
        session.close()
    def update_tags(self, id: int, newtags: str):
        session = Session()
        stmt = (
            update(self.image.__table__).
            where(self.image.__table__.c.id == id).
            values(tags=newtags)
        )
        session.execute(stmt)
        session.commit()
        session.close()

    def append_tags(self, id: int, newtags: str):
        session = Session()
        stmt = (
            update(self.image.__table__).
            where(self.image.__table__.c.id == id).
            values(tags=self.image.tags + newtags + ' ')
        )
        session.execute(stmt)
        session.commit()
        session.close()

    def execute_request(self, request):
        session.execute(request)
        session.commit()
        session.close()



Base.metadata.create_all(engine)
