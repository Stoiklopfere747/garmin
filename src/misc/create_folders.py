import os

# Define your desired folder structure
folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "scripts",
    "models",
    "logs",
    "reports/figures",
    "reports/tables",
    "tests",
]

# Create folders if they don't exist
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folder structure checked and created if missing.")
