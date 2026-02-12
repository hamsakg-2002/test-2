import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

specific_name = "Arjun Kumar"
pattern = rf'"name"\s*:\s*"{specific_name}"'
match = re.search(pattern, text)

if match:
    print(f"Found: {specific_name}")
else:
    print(f"{specific_name} not found")
