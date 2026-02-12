import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

ages = re.findall(r'"age"\s*:\s*(\d+)', text)

age_pattern = r'^(1[01]\d|[1-9]?\d|120)$'

for age in ages:
    if re.fullmatch(age_pattern, age):
        print(f"{age} -> VALID")
    else:
        print(f"{age} -> INVALID")
