import re
file_path = r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json"
with open(file_path, "r") as f:
    json_text = f.read()
pattern = r'"end_time"\s*:\s*"([0-2]?\d:[0-5]\d)"'
end_times = re.findall(pattern, json_text)
if end_times:
    print("End times found:", end_times)
else:
    print("No end times found")
