from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
#there is a whole lot of discussion about what 'metadata and engine' really are.
#I think this is a really good answer. 
#https://stackoverflow.com/questions/74755722/confused-between-engine-metadata-base-and-sessions-sqlalchemy-exc-unboundexecu
#in a nutshell, meta is an object that contains the information about tables.
#engine is an object/abastraction for database connection. 
#you need to connect to the database, hence an engine, and also you need to the database what table to create, hence metadata.

engine = create_engine('sqlite:///college.db', echo = True) #echo =True so all SQL statments are logged.
# MetaData is a container object that keeps together many different features of a database 
# (or multiple databases) being described
meta = MetaData() 

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer, ForeignKey('students.id')), 
   Column('postal_add', String), 
   Column('email_add', String)
)
meta.create_all(engine)


  




