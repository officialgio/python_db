from db_create import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Sequence

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))  #this puts a contraint on the value address.user_id can take
    user = relationship("User", back_populates="addresses") #notice that addresses is plural in back-populates!
    #because here user and address have a one-to-many relationship: a user has multiple addresses.
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    #id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    #addresses = relationship("Address", order_by=Address.id, back_populates="user")
    #addresses = relationship("Address", order_by=Address.id)

    #how to delete orphan entries, as you sometimes want to.
    addresses = relationship("Address", order_by=Address.id,
                     cascade="all, delete, delete-orphan", back_populates="user")
    #addresses = relationship("Address", back_populates='user',
    #                 cascade="all, delete, delete-orphan")


    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)





