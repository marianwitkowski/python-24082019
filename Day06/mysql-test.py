import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='54.229.158.46',
                                         database='kartoteka',
                                         user='kurspython',
                                         password='!kurspython$')
    print("Connect to DB")

    cursor = connection.cursor()
    sql = "SELECT id, imie, nazwisko, wiek, adres, data_rejestracji FROM osoby WHERE id<10 ORDER BY id DESC"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("Total records:",cursor.rowcount)
    for record in records:
        print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}\t{record[4]}\t{record[5]}")

    print("="*30)
    print("Pozyskaj rekord od ID=3")
    sql = "SELECT id, imie, nazwisko, wiek, adres, data_rejestracji FROM osoby WHERE id=3"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is None:
        print("Danych njet")
    else:
        print(row)

except Error as e:
    print(e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

