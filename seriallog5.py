import re

pattern = re.compile(r"(CPU|Memory|PCIe|USB)", re.IGNORECASE)

with open("serial_log.log", "r", errors="ignore") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
