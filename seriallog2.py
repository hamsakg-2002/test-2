import re

pattern = re.compile(r"POSTCODE=<(\d{4})>", re.IGNORECASE)


with open("serial_log.log", "r", errors="ignore") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
