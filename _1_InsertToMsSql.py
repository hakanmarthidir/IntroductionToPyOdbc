import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=sqlpython;UID=sa;PWD=123456789@')
cursor = connection.cursor()

cursor.execute("Insert Into Student(StudentFullName) Values ('Student 3')")

# Parametreli
cursor.execute("Insert Into Student(StudentFullName) Values (?)", 'Student 4')
connection.commit()

print("Inserted")
