from pymssql import _mssql, connect
import pandas as pd
import pyodbc

def main(server, user, password):
    with _mssql.connect(server=server, user=user, password=password, database="tempdb") as conn:

        # wiele wierszy
        # conn.execute_query('SELECT name FROM master.sys.databases')
        conn.execute_query('SELECT * FROM empl WHERE id=%d', 13)
        for row in conn:
            print(row)

        # jedne wiersz
        employeedata = conn.execute_row("SELECT * FROM employees WHERE id=%d", 13)

        # jedna liczba
        numemployees = conn.execute_scalar("SELECT COUNT(*) FROM employees")

        # nic nie zwraca
        conn.execute_non_query('CREATE TABLE persons(id INT, name VARCHAR(100))')


def main_cursor(server, user, password):
    with connect(server=server, user=user, password=password, database="tempdb") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT name FROM master.sys.databases')
            for row in cursor:
                print(row)

def main_pandas():
    conn = pyodbc.connect('Driver={SQL Server};'  # to może być np. {SQL Server Native Client 11.0}
                          'Server=ServerName;'
                          'Database=DatabaseName;'
                          'Trusted_Connection=yes;')
    df = pd.read_sql_query('SELECT * FROM products', conn)
    print(df)

if __name__ == "__main__":
    try:
        main(server="52.51.0.112", user="sa", password="...")
        main_cursor(server="52.51.0.112", user="sa", password="...")
    except _mssql.MSSQLDatabaseException as e:
        print("Błąd połączenia")
