import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

emails = re.findall(r'"email"\s*:\s*"([^"]+)"', text)
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
for email in emails:
    if re.fullmatch(email_pattern, email):
        print(f"{email} -> VALID")
    else:
        print(f"{email} -> INVALID")
