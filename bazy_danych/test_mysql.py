import pymssql
import pymysql.cursors

def main():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='my-secret-pw',
                                 db='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("sql......", (..., ...))
            # ... = cursor.fetchone()
            # .fetchmany(size=None)
            # .fetchall()
        connection.commit()


if __name__ == "__main__":
    main()