from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Change this URI to point to your local MongoDB instance
MONGODB_URI = "mongodb://localhost:27017/"

try:
    # Create a client and attempt to connect
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Force connection on a request as the connect=True parameter of MongoClient might not guarantee immediate connection
    client.admin.command("ping")
    print("✅ Successfully connected to local MongoDB!")

    # List available databases
    print("Databases:")
    for db_name in client.list_database_names():
        print(f" - {db_name}")

except ConnectionFailure as e:
    print("Could not connect to MongoDB:", e)
