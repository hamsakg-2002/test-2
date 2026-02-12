import re
with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r", encoding="utf-8") as file:
    text = file.read()
# Regex pattern to match only "name" values
name_pattern = r'"day_of_week"\s*:\s*"([^"]+)"'
names = re.findall(name_pattern, text)
for n in names:
    print(n)
