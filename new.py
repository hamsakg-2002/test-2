import json
import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()

phones = re.findall(r'\b\d{10}\b', text)

for p in phones:
    print(p)
