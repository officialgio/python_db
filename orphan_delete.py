from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import User, Address

Session = sessionmaker(bind = engine)
session = Session()

if __name__ == "__main__":
    jack = session.get(User, 5)

    #join
    #result = session.query(User).join(Address).filter(Address.email_address=="jack@google.com")
    #result.all()

    #how cascade delete works
    session.delete(jack)
    session.commit()

    #there should be no orphan entries left.
    result = session.query(Address).filter((Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])))
    print(result.all())

    session.close()
