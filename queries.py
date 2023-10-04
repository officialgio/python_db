
from db_create import User
from db_create import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()
result = session.query(User).all()

for row in result:
       print ("Name: ",row.name, "Fullname:",row.fullname, "Nickname:",row.nickname, "Addresses:", row.addresses)

result = session.query(User).filter(User.id!=2)

for row in result:
       print("Name: ",row.name, "Fullname:",row.fullname, "Nickname:",row.nickname, "Addresses:", row.addresses)

