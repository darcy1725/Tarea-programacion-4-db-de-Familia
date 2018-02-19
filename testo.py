import sqlite3
import sys

def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Addess, Age FROM Persona")
    for row in result:
        print("ID :", row[0])
        print("FName :", row[1])
        print("LName :", row[2])
        print("Address :", row[3])
        print("Age :", row[4])

    except sqlite3.OperationalError:
        print("The Table doesn't exist")

db_conn = sqlite3.connect("test.db")

print("data base created")

theCursor = db_conn.cursor()

 db_conn.execute("DROP TABLES IF EXIST Persona")
 db_conn.commit()
try:
db_conn.execute("CREATE TABLE Persona(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Address TEXT, Age INTEGER NOT NULL);")

    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be created")

print("table created")

db_conn.execute("INSTERT INTO Persona (FName, LName, Address, Age) VALUES('Darcy', 'Smith', 1996, '123 main St')")

db_conn.commit()

try:
db_conn.execute("CREATE TABLE Familia(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, IDPadre TEXT NOT NULL, IDHijo TEXT NOT NULL, Relacion TEXT NOT NULL);")

    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be created")

print("table created")

db_conn.execute("INSTERT INTO Familia (IDPadre, IDHijo, Relacion) VALUES('Pedro', 'Paula','Hija')")

db_conn.commit()


printDB()

db_conn.close

print("data base closed")