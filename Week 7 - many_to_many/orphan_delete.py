from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()

john = session.query(Order).filter(Order.customer_name == "John Smith").first()
session.delete(john)
session.commit()

