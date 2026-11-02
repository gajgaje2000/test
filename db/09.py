import json
from pymongo import MongoClient

def show(cursor):
    for doc in cursor:
        print(doc)

client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

db = client["college"]
col = db["students"]
col.drop()

col.insert_one({"name": "Amit", "major": "CS",
                "enrollments": [{"course": "Math", "marks": 85}]})
col.insert_many([
    {"name": "Riya", "major": "IT",
     "enrollments": [{"course": "Math", "marks": 70}, {"course": "DBMS", "marks": 90}]},
    {"name": "Karan", "major": "CS",
     "enrollments": [{"course": "DBMS", "marks": 60}]},
])
print(db.list_collection_names())

show(col.find())
print(col.find_one({"name": "Amit"}))
show(col.find({"major": "CS"}))
show(col.find().sort("name", -1).skip(1).limit(2))

show(col.aggregate([
    {"$group": {"_id": "$major", "count": {"$sum": 1}}}
]))

show(col.aggregate([
    {"$unwind": "$enrollments"},
    {"$group": {"_id": "$enrollments.course", "avg_marks": {"$avg": "$enrollments.marks"}}}
]))

show(col.find({"enrollments": {"$elemMatch": {"course": "Math", "marks": {"$gt": 80}}}}))

col.update_one({"name": "Amit"}, {"$set": {"major": "AI"}})
col.update_one({"name": "Amit"}, {"$push": {"enrollments": {"course": "DBMS", "marks": 75}}})
col.update_one({"name": "Riya", "enrollments.course": "Math"},
               {"$set": {"enrollments.$.marks": 95}})
col.update_one({"name": "Amit"}, {"$pull": {"enrollments": {"course": "DBMS"}}})
col.update_one({"name": "Neha"}, {"$set": {"major": "CS"}}, upsert=True)
col.replace_one({"_id": 100}, {"_id": 100, "name": "Tina"}, upsert=True)

col.delete_one({"name": "Karan"})
col.delete_many({"major": "CS"})

data = list(col.find({}, {"_id": 0}))
with open("students.json", "w") as f:
    json.dump(data, f)

with open("students.json") as f:
    col.insert_many(json.load(f))

col.rename("pupils")
db["pupils"].rename("students")
