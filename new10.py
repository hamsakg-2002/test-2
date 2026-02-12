import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

phones = re.findall(r'"phone"\s*:\s*"([^"]+)"', text)

phone_pattern = r'^\+?\d{1,3}[- ]?\d{10}$'

for phone in phones:
    if not  re.fullmatch(phone_pattern, phone):
        print(f"{phone} ->INVALID")
