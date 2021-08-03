import sqlite3

db = sqlite3.connect("DATABASE.db")

"""
IMPORTANT: strings in SQL queries should use single quote ('') instead of double quote (""). 
"""

################
# CREATE TABLE #
################
print("[CREATE TABLE]")

query = """
        CREATE TABLE 'Person' (
        'PersonID' INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
        'Name' TEXT NOT NULL,
        'Age' INTEGER NOT NULL
        )
        """

db.execute(query)

query = """
        CREATE TABLE 'Employee' (
        'EmployeeID' INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
        'HoursWorked' REAL NOT NULL
        )
        """

db.execute(query)

query = """
        CREATE TABLE 'Company' (
        'PersonID' INTEGER NOT NULL,
        'EmployeeID' INTEGER NOT NULL,
        PRIMARY KEY('PersonID', 'EmployeeID'),
        FOREIGN KEY('PersonID') REFERENCES Person('PersonID'),
        FOREIGN KEY('EmployeeID') REFERENCES Employee('EmployeeID')
        )
        """

db.execute(query)

db.commit()

###############
# INSERT INTO #
###############
print("[INSERT INTO]")

with open("TEST DATA.txt", "r") as f: # read file
    read_header = f.readline()[:-1].split(",")
    read_person = []
    for line in f:
        if line[-1] == "\n":
            line = line[:-1]
        if len(line.split(",")) > 2: # name has comma
            temp = line.split("\"")[1:]
            temp[1] = temp[1][1:]
        else:
            temp = line.split(",")
        temp[1] = int(temp[1])
        read_person.append(temp)
    f.close()

query = """
        INSERT INTO Person('Name', 'Age')
        VALUES(?, ?)
        """

for person in read_person:
    db.execute(query, person)

db.commit()

###############
# SELECT FROM #
###############
print("[SELECT FROM]")

query = """
        SELECT *
        FROM Person
        WHERE Person.Age < ?
        """

result = list(db.execute(query, (50, )))

for person in result:
    print(person)

##############
# UPDATE SET #
##############
print("[UPDATE SET]")

query = """
        UPDATE Person
        SET Name = ?, Age = ?
        WHERE PersonID = ?
        """

db.execute(query, ("Skittles", 1, 1))

db.commit()

query = """
        SELECT *
        FROM Person
        WHERE Person.PersonID = ?
        """

result = list(db.execute(query, (1, )))

print(result[0])

###############
# DELETE FROM #
###############
print("[DELETE FROM]")

query = """
        DELETE FROM Person
        WHERE Person.PersonID = ?
        """

for i in range(1, 11):
    db.execute(query, (i, ))

db.commit()

query = """
        SELECT *
        FROM Person
        """

result = list(db.execute(query))

print("Number of people in table Person:", len(result))

##############
# DROP TABLE #
##############
print("[DROP TABLE]")
query = """
        DROP TABLE Company
        """

db.execute(query)

query = """
        DROP TABLE Employee
        """

db.execute(query)

query = """
        DROP TABLE Person
        """

db.execute(query)

db.commit()

db.close()
