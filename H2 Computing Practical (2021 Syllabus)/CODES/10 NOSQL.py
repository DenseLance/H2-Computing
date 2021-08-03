import json
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
client.drop_database("db")
db = client.get_database("db")
crimes = db.get_collection("crimes")

##db = client["db"]
##crimes = db["crimes"]

#############
# json.load #
#############
print("[json.load]")

with open("TEST DATA 2.json", "r") as f:
    data = json.load(f)
    f.close()

print("Data from json:", data)

###############
# insert_many #
###############
print("[insert_many]")

crimes.insert_many(data)

##############
# insert_one #
##############
print("[insert_one]")

crimes.insert_one({"_id": 11, "accused": "Pablo Skittles", "gender": "M", "age": 33, "records": [{"type": "Kidnapping", "victims": ["Beluga"]}]})

########
# find #
########
print("[find]")

# $gt/lt
result = list(crimes.find({"age": {"$gt": 30}}, {"accused": 1, "_id": 0}))

print("Names of accused with age > 30:")

for accused in result:
    print(accused)

# $and, $in, .$.
result = list(crimes.find({"$and": [{"records.type": {"$in": ["Kidnapping", "Terrorism"]}}, {"gender": "M"}]}, {"records.$.victims": 1, "_id": 0}))

print("Names of victims of kidnapping or terrorism incidents caused by male accused(s):")

for accused in result:
    print(accused)

# $or, $size, $exists
result = list(crimes.find({"$or": [{"records.victims": {"$size": 2}}, {"nationality": {"$exists": False}}]}, {"accused": 1, "_id": 0}))

print("Names of accused who have crime record that involves 2 victims or do not have nationality:")

for accused in result:
    print(accused)

###################
# count_documents #
###################
print("[count_documents]")

result = crimes.count_documents({"records.type": "Murder"})

print("Number of accused that have committed murder:", result)

########
# sort #
########
print("[sort]")

result = crimes.find({}, {"accused": 1, "age": 1, "_id": 0}).sort([("age", 1), ("accused", -1)])

print("Sort by age of accused in ascending order, followed by name of accused in descending order:")

for accused in result:
    print(accused)

###############
# update_many #
###############
print("[update_many]")

print("Nationality of all accused before update_many:")

result = crimes.find({}, {"accused": 1, "nationality": 1, "_id": 0})

for accused in result:
    print(accused)

# $set
crimes.update_many({}, {"$set": {"nationality": "Singapore"}})

print("Nationality of all accused after update_many:")

result = crimes.find({}, {"accused": 1, "nationality": 1, "_id": 0})

for accused in result:
    print(accused)

##############
# update_one #
##############
print("[update_one]")

crimes.update_one({"accused": "Pablo Skittles"}, {"$unset": {"nationality": 0}})

print("Nationality of all accused after removing nationality of Pablo Skittles:")

result = crimes.find({}, {"accused": 1, "nationality": 1, "_id": 0})

for accused in result:
    print(accused)

###############
# delete_many #
###############
print("[delete_many]")

crimes.delete_many({"nationality": "Singapore"})

print("Records after deleting all Singaporeans:")

result = crimes.find({}, {"accused": 1, "nationality": 1, "_id": 0})

for accused in result:
    print(accused)

##############
# delete_one #
##############
print("[delete_one]")

crimes.delete_one({"accused": "Pablo Skittles"})

print("Records after deleting Pablo Skittles:")

result = crimes.find({}, {"accused": 1, "nationality": 1, "_id": 0})

for accused in result:
    print(accused)

client.close()
