import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=sqlpython;UID=sa;PWD=123456789@', autocommit=False)
cursor = connection.cursor()

params = ("Student Proc")
cursor.execute("{CALL InsertStudent (?)}", params)
# Parametresiz olsaydı cursor.execute("{CALL InsertStudent}")

connection.commit()
connection.close()
print("Called")
