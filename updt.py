from db_create import User
from db_create import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()
session.query(User).filter(User.id!=2).update({User.name:"Dr."+User.name})

#session.rollback()
session.commit()
