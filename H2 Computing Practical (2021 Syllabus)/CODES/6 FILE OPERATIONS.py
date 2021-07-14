from random import randint

header = ["Name", "Age"]
name = ["Bob", "Tom", "Jerry", "Jesus", "\"Korean, Jesus\"", "Maple", "Lisa", "Jack", "Moby", "Obama"]
age = [randint(1, 100) for _ in range(10)]
person = dict(zip(name, age))

print("Headers:", header)
print("Person:", person)
print()

with open("TEST DATA.txt", "w") as f: # write file
    f.write(",".join(header))
    for name in person:
        f.write("\n" + name + "," + str(person[name]))
    f.close()

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

print("Read headers:", read_header)
print("Read person:", read_person)
print()
