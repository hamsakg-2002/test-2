import json
import re
with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\swathi_test.json","r") as file:
     text = file.read()
phones = re.findall(r'"phone"\s*:\s*:(\+?\d{1-3}\d[- ]?\d{10})"',text)
with open("C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hamsa\\regex.txt","w") as outfile:
     for p in phones:
          outfile.write(p + "\n")
     print("phone numbers")