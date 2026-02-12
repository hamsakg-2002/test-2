import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

names = re.findall(r'"name"\s*:\s*"([^"]+)"', text)

name_pattern = r'^[A-Za-z]+(?: [A-Za-z]+)*$'

for name in names:
    if re.fullmatch(name_pattern, name):
        print(f"{name} = VALID")
    else:
        print(f"{name} = INVALID")
