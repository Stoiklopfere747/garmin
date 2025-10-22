import os
import json
from datetime import datetime, timedelta
from dateutil.parser import parse
from pymongo import MongoClient

# ---------------------------
# CONFIG
# ---------------------------
DATA_DIR = r"C:\Users\nfischer\git\garmin\data\external"
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "garmin"
COLLECTION_NAME = "bike_activities"

# ---------------------------
# CONNECT TO MONGODB
# ---------------------------
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# ---------------------------
# HELPER FUNCTIONS
# ---------------------------
def parse_date(activity_json):
    """Try to parse the activity start date."""
    start_time_str = activity_json.get("startTimeLocal") or activity_json.get("startTimeGMT")
    if start_time_str:
        try:
            return parse(start_time_str)
        except Exception as e:
            print(f"Failed to parse date {start_time_str}: {e}")
    return None

def is_bike_activity(activity_json):
    """Check if the activity type is cycling."""
    return activity_json.get("activityTypeDTO", {}).get("typeKey") == "cycling"

# ---------------------------
# PROCESS FILES
# ---------------------------
two_weeks_ago = datetime.now() - timedelta(weeks=2)
count_inserted = 0

for fname in os.listdir(DATA_DIR):
    if fname.lower().endswith(".json") and "summary" in fname.lower():
        full_path = os.path.join(DATA_DIR, fname)
        with open(full_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Skipping {fname}, JSON error: {e}")
                continue

        date = parse_date(data)
        if not date:
            print(f"Skipping {fname}, could not parse date")
            continue

        if is_bike_activity(data) and date >= two_weeks_ago:
            print(f"Inserting {fname} | {date} | Cycling activity")
            collection.insert_one(data)
            count_inserted += 1
        else:
            print(f"Skipping {fname} | {date} | Not a cycling activity or too old")

print(f"Done! Inserted {count_inserted} bike activities into MongoDB.")
