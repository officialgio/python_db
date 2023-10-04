from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #you may think of this Base class as the base class for all the models you want to create. 
from models import *
Base.metadata.create_all(engine)