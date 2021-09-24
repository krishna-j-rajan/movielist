import mysql.connector
db_connection = mysql.connector.connect(
   host="localhost",
   user="krishna",
   passwd="k@tt46v@zha.c0m",
   database="NAME"
  )
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE mymovielist (Slno INT, movie_name VARCHAR(255),actor_name VARCHAR(255),actress_name VARCHAR(255),year_of_release INT,director_name VARCHAR(255))")
insert_stmt= ("INSERT INTO customers(Slno, movie_name, actor_name, actress_name, year_of_release, director_name)"
   "VALUES (%d,%s,%s,%s,%d,%s)")
data=[
  (1,'Quills', 'Geoffrey Rush','Kate Winslet',2000,'Philip Kaufman'),
  (2,'Unlikely Hero', 'Jeff Daniels','Emma Stone',2009,'Kieran Mulroney'),
  (3,'Bernie', 'Jack Black','Jack Black',2011,'Richard Linklater'),
  (4,'The Experts', 'John Travolta','Arye Gross',1989,'Dave Thomas'),
  (5,'Mike Nichols', 'Jack Nicholson','Meryl Streep',1986,'Dave Thomas')
]

try:
   db_cursor.executemany(insert_stmt,data)
   db_connection.commit()

except:
   
   db_connection.rollback()
cursor = db.cursor()
query1 = "SELECT * FROM mymovielist"
query = "SELECT movie_name, actor_name FROM mymovielist"

cursor.execute(query1)
cursor.execute(query)


data = cursor.fetchall()


for pair in data:
    print(pair)


print("Data inserted")
db_connection.close()
