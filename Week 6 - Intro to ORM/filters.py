from db_create import User, Address
from db_create import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()


session.query(User).filter(User.id.in_([1,3]))

session.query(User).filter(User.id>2, User.name.like('Raj%'))

#and or, when you want to filter by a few conditions at the same time

from sqlalchemy import and_
session.query(User).filter(and_(User.id>2, User.name.like('Raj%')))

from sqlalchemy import or_
result = session.query(User).filter(or_(User.id>2, User.name.like('Ra%')))

#join query
result = session.query(User).join(Address).filter(Address.email_address.like('Ja%'))
print(result.all())




