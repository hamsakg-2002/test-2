import re

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r") as file:
    text = file.read()

age = tuple(re.findall(r'"age"\s*:\s*(\d+)', text))
print(age)
