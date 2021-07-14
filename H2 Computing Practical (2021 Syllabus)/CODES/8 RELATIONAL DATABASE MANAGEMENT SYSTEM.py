import sqlite3

db = sqlite3.connect("DATABASE.db")

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
        INSERT INTO Person("Name", "Age")
        VALUES(?, ?)
        """

for person in read_person:
    db.execute(query, person)

db.commit()
db.close()
