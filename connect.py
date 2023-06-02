#!/usr/bin/env python
import mariadb
import sys

# Connect to MariaDB Platform
try:
 conn = mariadb.connect(
  user="sagelicuser",
  password="sagelicpw",
  host="161.79.58.242",
  port=3306,
  database="sagelicbd"
 )
except mariadb.Error as e:
 print(f"Error connecting to MariaDB Platform: {e}")
 sys.exit(1)

# Get Cursor
							
cur = conn.cursor()
sql = "SELECT id, descricao FROM modulo"
cur.execute(sql)
#result = cur.fetchall()

for (id, descricao) in cur:
 print(f"  {id}, {descricao}  ")

conn.close()
