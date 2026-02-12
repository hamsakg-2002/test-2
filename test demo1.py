import json
import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()
age = re.findall(r'"age"\s*:\s*(\d+)', text)
for a in age:
    print(a)