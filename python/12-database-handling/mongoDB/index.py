from pymongo import MongoClient
try:
    client = MongoClient(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=5000
    )

    client.admin.command("ping")
    print("Connected successfully!")

except Exception as e:
    print(f"Connection failed: {e}")

mydb = client["my_database"]
mycollection = mydb["myTable"]

record = {
    "title": "MongoDB and Python",
    "description": "MongoDB is no SQL database",
    "tags": ["mongodb", "database", "NoSQL"],
    "viewers": 104
}

rec = mycollection.insert_one(record)