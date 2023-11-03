from sqlalchemy.orm import sessionmaker
from db_create import engine
from models import *

Session = sessionmaker(bind = engine)
session = Session()
#first, create a bunch of items.
tshirt, mug, hat, crowbar = (
    Item("SA T-Shirt", 10.99),
    Item("SA Mug", 6.50),
    Item("SA Hat", 8.99),
    Item("SA Crowbar", 16.99),
)
session.add_all([tshirt, mug, hat, crowbar])
session.commit()

# create an order. 
order = Order("John Smith")

# add three OrderItem associations to the Order and save them
order.order_items.append(OrderItem(mug))
order.order_items.append(OrderItem(crowbar))
order.order_items.append(OrderItem(hat))

order2 = Order("Sunyung Lee")
order2.order_items.append(OrderItem(tshirt))
order2.order_items.append(OrderItem(mug))

session.add(order)
session.add(order2)
session.commit()

