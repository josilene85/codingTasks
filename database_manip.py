""" This program will display a table called python_programming with the following information:
(55, 'Carl Davis', 65)
(66, Dennis Fredrickson, 88)
(77, 'Jane Richards', 80)
(12, 'Peyton Sawyer', 45)
(2, 'Lucas Brooke', 99)

Next, all records with a grade between 60 and 80 were selected.
Next, Carl Davis’s grade were changed to 65.
Following, data Dennis Fredrickson’s row deleted.
lastly, all students with an id greater than 55 changed to grade of 80.
"""

import sqlite3

db = sqlite3.connect('grade_db.db')

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS python_programming (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)")
print('Table Created' + "\n")

cursor.execute("INSERT INTO python_programming(id, name, grade) VALUES(55, 'Carl Davis', 61)")
cursor.execute("INSERT INTO python_programming(id, name, grade) VALUES(66, 'Dennis Fredrickson', 88)")
cursor.execute("INSERT INTO python_programming(id, name, grade) VALUES(77, 'Jane Richards', 78)")
cursor.execute("INSERT INTO python_programming(id, name, grade) VALUES(12, 'Peyton Sawyer', 45)")
cursor.execute("INSERT INTO python_programming(id, name, grade) VALUES(2, 'Lucas Brooke', 99)")
print('All user´s inserted' + "\n")

cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")

cursor.execute("UPDATE python_programming SET grade = 65 WHERE id = 55")
cursor.execute("DELETE FROM python_programming WHERE id = 66")
cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")
cursor.execute("SELECT * FROM python_programming")

db.commit()

db.close()