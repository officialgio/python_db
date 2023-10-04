from db_configure import students, addresses
from db_configure import engine
# a single insertion
ins = students.insert().values(name = 'Dennis', lastname = 'Cooper')


#multiple insertion
student_group = [
{'name':'Rachel', 'lastname' : 'Green'},
{'name':'Newt','lastname' : 'Jackson'},
{'name':'Jen','lastname' : 'Li'},
{'name':'Pauline','lastname' : 'Cooper'},
]

ins_group = students.insert().values(student_group)


#create a connection 
conn = engine.connect()

#execute all the statements
result = conn.execute(ins)
result_group = conn.execute(ins_group)

result.inserted_primary_key

conn.execute(addresses.insert(), [
{'st_id':1, 'postal_add':'Lituanica ave', 'email_add':'Cooper3@gmail.com'},
{'st_id':1, 'postal_add':'West Adam St', 'email_add':'DennisC5@gmail.com'},
{'st_id':2, 'postal_add':'Norman ave', 'email_add':'Green1@gmail.com'},
{'st_id': 2, 'postal_add': 'Roath park St', 'email_add': 'Green3@neiu.edu'},
{'st_id': 3, 'postal_add': 'Jackson St', 'email_add': 'Newt37@iit.edu'},
{'st_id': 5, 'postal_add': 'Sox 35th', 'email_add': 'Pcooper25@neiu.edu'},

])