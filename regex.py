import json

file_path = "C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)


name_age_list = [(u["name"], u["age"]) for u in data["users"]]

print(name_age_list)


