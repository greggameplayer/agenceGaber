import pyodbc


def ConnectToDatabase():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AgenceGaber;Trusted_Connection=yes;')
    conn.setencoding(encoding='utf-8')
    return conn


def Main():
    conn = ConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("select * from circuit")
    row = cursor.fetchone()
    print('name:', row[1])          # access by column index (zero-based)
    print('name:', row.IdCircuit)
