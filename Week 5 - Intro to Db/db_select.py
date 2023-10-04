from db_configure import students, engine

if __name__ == "__main__":
   #select rows 
   s = students.select()
   conn = engine.connect()
   result = conn.execute(s)

   #result.fetchall()  #like pop in dictionry or list while you are not actually deleting entries in the table
   #result.fetchone()


   #where clause
   s = students.select().where(students.c.id>2)
   result = conn.execute(s)
   result.fetchone()  #like pop or inject.

   for row in result.fetchall():
      print(row)

