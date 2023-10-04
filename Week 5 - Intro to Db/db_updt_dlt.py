from db_configure import students, engine

# always, make a statment first, and then execute it.
conn = engine.connect()

updt=students.update().where(students.c.lastname=='Green').values(lastname='Bing')
conn.execute(updt)

s = students.select()
result = conn.execute(s)
print(result.fetchall())   #loading all the entries 


dt = students.delete().where(students.c.id > 4) 
conn.execute(dt)
s = students.select()
result = conn.execute(s)
print(result.fetchall())   #now that no 5 is removed. :loading the rest entries



