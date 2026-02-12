import json
file_path = r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json"
output_path = r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\regex.txt"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
sunrise_day_of_week_list = {
    (u["tithi"]["name"], u["day_of_week"])
    for u in data["data"]
}

# write to txt file
with open(output_path, "w", encoding="utf-8") as out:
    for tithi, day in sunrise_day_of_week_list:
        out.write(f"{tithi} - {day}\n")

print("Data written to sunrise_day_of_week.txt successfully")
