import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'movies',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
print("connected")
cursor = cnx.cursor();
cursor.execute("show databases");
for x in cursor:
  print(x)

cnx.close()





