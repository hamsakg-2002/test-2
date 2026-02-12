import json
import re
with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()
phones = re.findall(r'"phone"\s*:\s*"(\+?\d{1,3}[- ]?\d{10})"', text)
with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\hamsa\univision.txt", "w") as outfile:
    for p in phones:
        outfile.write(p + "\n")

print("Phone numbers ")

