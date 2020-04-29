import pyodbc


def ConnectToDatabase():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AgenceGaber;Trusted_Connection=yes;')
    conn.setencoding(encoding='utf-8')
    return conn


def Main():
    conn = ConnectToDatabase()
    cursor = conn.cursor()
    cursor.execute("select * from circuit")
    rows = cursor.fetchall()
    for row in rows:
        print(row[1], row.IdCircuit)
    cursor.close()
    conn.close()
