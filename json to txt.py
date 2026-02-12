import json
import re


text = open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json", "r").read()

phones = re.findall(r'"phone"\s*:\s*"(\+?\d{1,3}[- ]?\d{10})"', text)

with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\hamsa\\regex.txt", "w") as f:
    for phone in phones:
        f.write(phone + "\n")

print("to txt file")
