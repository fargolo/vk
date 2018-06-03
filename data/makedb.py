import sqlite3

conn = sqlite3.connect("patients.sqlite")
c = conn.cursor()
c.execute("CREATE TABLE patients (first_name varchar(255),last_name varchar(255), age int);")
conn.commit()
conn.close()
