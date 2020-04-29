import pyodbc


def ConnectToDatabase():
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:greggameplayer.database.windows.net,1433;Database=AgenceGaber;Uid=greggameplayer;Pwd=Gg123456;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
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
