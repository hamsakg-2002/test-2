import json
file_path = r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

sunrise_day_of_week_list = {
    (u["tithi"]["name"], u["day_of_week"])
    for u in data["data"]
}

sunrise_day_of_week_tuple = tuple(sunrise_day_of_week_list)

print(sunrise_day_of_week_tuple)


