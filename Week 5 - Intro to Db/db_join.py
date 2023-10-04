from sqlalchemy import join
from sqlalchemy.sql import select
from db_configure import students, addresses, engine

conn = engine.connect()
#let us find out the people who use their first name for their email address. 
j = students.join(addresses, addresses.c.email_add.like(students.c.name + '%'))
s = select([students]).select_from(j)
#select a specific column
s_column = select([students.c.lastname]).select_from(j)
a_column = select([addresses]).select_from(j)

result = conn.execute(s)
print(result.fetchall())

result = conn.execute(s_column)
print(result.fetchall())