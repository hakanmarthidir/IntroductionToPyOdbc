import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=sqlpython;UID=sa;PWD=123456789@')
cursor = connection.cursor()

cursor.execute("delete from student where StudentId = ?", '4')
print(cursor.rowcount, 'Student was deleted')

deleted = cursor.execute("delete from student where StudentId = ?", '3').rowcount
if deleted > 0:
    print("OK")
else:
    connection.rollback()

connection.commit()