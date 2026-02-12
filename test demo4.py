import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()

pattern = r'"name"\s*:\s*"([^"]+)"[\s\S]*?"phone"\s*:\s*"(\+?\d{1,3}[- ]?\d{10}|\d{10})"'

result = tuple(re.findall(pattern, text))

print(result)
