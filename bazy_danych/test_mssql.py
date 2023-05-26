from pymssql import _mssql

def main(server, user, password):
    with _mssql.connect(server=server, user=user, password=password, database="tempdb") as conn:
        conn.execute_query('SELECT name FROM master.sys.databases')
        for row in conn:
          print(row)

if __name__ == "__main__":
    try:
        main(server="localhost", user="sa", password="")
    except _mssql.MSSQLDatabaseException as e:
        print("Nie działa")

    try:
        main(server="...", user="sa", password="...")
    except _mssql.MSSQLDatabaseException as e:
        print("Nie działa")
