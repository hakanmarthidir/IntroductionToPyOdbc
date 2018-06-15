import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=sqlpython;UID=sa;PWD=123456789@')
cursor = connection.cursor()

cursor.execute("Select * From Student")
row = cursor.fetchall()

for c in row:
    print(c)
    print(c.StudentFullName)
    print(c[0])


#Tek Satır okumak için kullanılır.
cursor.execute("Select * From Student Where StudentId = 1")
row = cursor.fetchone()
print(row)

#Tek Satır Tek Sutun için kullanılır. Yani ilk satırın ilk sutununu doner.
#Eger cevap yoksa None doner.
#.fetchone()[0] gibi kullanmak yerine asagidaki gibi sorgularda fetchval kullanılır. 

cursor.execute("Select Count(*) From Student")
row2 = cursor.fetchval()
print(row2)