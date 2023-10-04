from db_create import User
from db_create import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()

print(session.query(User).first())
print(session.query(User).all())

try:
    session.query(User).one()
except:
    raise ValueError('more than one objects satisfying the condition')