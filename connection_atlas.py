from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://nadine:Stoiklopfere01!mongodb@cluster0.ncdfrbh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)