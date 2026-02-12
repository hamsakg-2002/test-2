import json
import re
with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()
pattern = r'"name"\s*:\s*"([^"]+)"\s*,\s*"age"\s*:\s*(\d+)'
result = tuple(re.findall(pattern, text))
print(result)