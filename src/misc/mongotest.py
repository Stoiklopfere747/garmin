from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    print(client.server_info())  # will throw if not running
except Exception as e:
    print("MongoDB not running:", e)
