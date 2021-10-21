from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, and_, desc

class Database:
    def __init__(self, config):
        engine = create_engine(f"postgresql+psycopg2://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@db:5432/{config['POSTGRES_DB']}")

        Session = sessionmaker(bind=engine)

        # create a Session
        self.session = Session()
    
    def write(self, obj):
        self.session.add(obj)
        self.session.commit()

    def count(self, obj, column):
        resp = self.session.query(obj).order_by(desc(column)).limit(10).all()
        return resp

    def get_last(self, obj, column):
        print(self.session.query(obj).order_by(desc(column)).first())