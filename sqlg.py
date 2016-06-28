import sqlite3 

conn = sqlite3.connect("new.db")


with conn as connection :
	c = connection.cursor()

	c.execute("""CREATE TABLE regions
		(city TEXT, region , TEXT)
		""")		
	cities = [
	('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000),
	('Dallas', 'TX', 4200000),
	('Boston', 'MA', 600000),
	('Los Angeles', 'CA', 38000000),
	('Houston', 'TX', 2100000),
	('Philadelphia', 'PA', 1500000),
	('San Antonio', 'TX', 1400000),
	('San Diego', 'CA', 130000),
	('Dallas', 'TX', 1200000),
	('San Jose', 'CA', 900000),
	('Jacksonville', 'FL', 800000),
	('Indianapolis', 'IN', 800000),
	('Austin', 'TX', 800000),
	('Detroit', 'MI', 700000)
	]

	c.executemany('INSERT INTO regions VALUES(?, ?, ?)', cities)
	c.execute("SELECT * FROM regions ORDER BY region ASC")
	rows = c.fetchall()

	for r in rows:
		print(r[0],r[1])


#Close the database connection
conn.close()