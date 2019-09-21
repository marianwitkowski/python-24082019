import mysql.connector
from mysql.connector import Error

age_from = None
while type(age_from)!=float:
    try:
        age_from = float(input("Countries with life expectancy from age: "))
    except ValueError as e:
        print(e)
        print("You have provided the wrong value - please provide \"age from\" once again")
print(type(age_from))

age_till = 0
while type(age_till)!=float or age_till<age_from:
    try:
        age_till= float(input("Countries with life expectancy till age: "))
        if age_till<age_from:
            print("You moron :) !! \"age till\" must be greater then age from !!")
    except ValueError as e:
        print(e)
        print("You have provided the wrong value - please provide \"age till\" once again")


try:
    connection = mysql.connector.connect(host="35.156.38.123",
                                         database='db02',
                                         user='user02',
                                         password='TE29S7')
    print("connect to DB")
    connection.autocommit = True #wszelkie updaty do bazy maja skutek natychmiastowy

    cursor = connection.cursor()  #potrzebne zeby chodzic po tabeli, uchwyt do danych
    sql = (f"SELECT Code, Name, Continent, Region,LifeExpectancy FROM country WHERE LifeExpectancy BETWEEN {age_from} "
           f"AND {age_till} ORDER BY LifeExpectancy ASC")

    print(sql)

    cursor.execute(sql)
    records = cursor.fetchall()
    print("Total records:", cursor.rowcount)
    for record in records:
        print(f"{record[0]:5s}\t{record[1]:30s}\t\t{record[2]:15s}\t\t{record[3]:30s}\t{record[4]}")


except Error as e:
    print(e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()