from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()

simple_query = session.query(Order).filter(Order.customer_name == 'Sunyung Lee').all()
for order in simple_query:
    print(order)

#this is one way to do join query. 
orders= session.query(Order, Item).filter(Item.price <= 8.0).all()
for order in orders:  #this is actually a query that fetches you both order and item. 
    
    print(order) #order is a tuple. 
    print(order[0])


#result = session.query(Order).join(Item).filter(OrderItem.price<=8.0)
#print(result.all())

#this is a better way to do join query. It is more specific. 
result = session.query(Order).join(OrderItem).filter(OrderItem.price<=8.0).all()
result[0].order_items

