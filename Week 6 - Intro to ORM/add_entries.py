from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import User, Address

Session = sessionmaker(bind = engine)
session = Session()
if __name__ == "__main__":
    ed_user = User(name='Ed', fullname='Edward Jones', nickname='Eddy')
    session.add(ed_user)
    session.commit()

    session.add_all([
    User(name = 'Cristina', fullname = 'Christian Nolan', nickname = 'Crist'), 
    User(name = 'Rajender', fullname = 'Rajender Minnah', nickname = 'Raj'), 
    User(name = 'Ricky', fullname = 'Ricky Van Vliet', nickname = 'Rick')]
    )
    jack = User(name='Jack', fullname='Jack Bean', nickname='Jackie')
    jack.addresses = [
                 Address(email_address='jack@google.com'),
                 Address(email_address='j25@yahoo.com')]
    session.add(jack)
    session.commit()
