import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Documents\hamsa\panchang_data.json", "r", encoding="utf-8") as file:
    text = file.read()

# Regex pattern to match only "name" values
rise=r'"([0-2]?\d:[0-5]\d)"'

names = re.findall(rise, text)

for n in names:
    print(n)