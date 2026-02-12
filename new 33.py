import json
import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()

name = re.findall(r'"name"\s*:\s*"([^"]+)"', text)


for p in name:
    print(p)


