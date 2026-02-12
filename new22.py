import json
import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()
email = re.findall(r'"email"\s*:\s*"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"', text)

for p in email:
    print(p)

