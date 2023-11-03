from datetime import datetime

from sqlalchemy import and_, Column, DateTime, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
from db_create import Base

class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    customer_name = Column(String(30), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.now())
    order_items = relationship(
        "OrderItem", cascade="all, delete-orphan", backref="order"
    )


    def __init__(self, customer_name):
        self.customer_name = customer_name

    def __repr__(self):
        return "<Order(order_id='%s', customer_name='%s', order_date='%s')>" % (
                                self.order_id, self.customer_name, self.order_date) 
    




class Item(Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True)
    description = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, description, price):
        self.description = description
        self.price = price

    def __repr__(self):
        return "<Item(item_id='%s', description='%s', price='%s')>" % (
                                self.item_id, self.description, self.price)




class OrderItem(Base): #you may think of an object from this class as an 'ordered item' 
    #in the sense that it is an item that is purchased with a certain order.
    #orderitem is very different than other classes we've seen so far.
    #it has two primary keys!
    #you probably want to use a constructor to well define a way to instantiate an object. 
    
    __tablename__ = "orderitem"

    order_id = Column(Integer, ForeignKey("order.order_id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("item.item_id"), primary_key=True)
    price = Column(Float, nullable=False)

    def __init__(self, item, price=None):
        self.item = item
        self.price = price or item.price

    item = relationship(Item)
    #item = relationship(Item, lazy="joined")
    
    def __repr__(self):
        return "<Orderitem(order_id='%s', item_id='%s',price='%s')>" % (
                                self.order_id, self.item_id, self.price)

    

'''
association_table = Table(
    "association",
    Base.metadata,
    Column("order_id", ForeignKey("order.order_id"), primary_key=True),
    Column("item_id", ForeignKey("item.item_id"), primary_key=True),
)
'''