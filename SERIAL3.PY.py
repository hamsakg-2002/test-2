import re

pattern = re.compile(r"(RESET|REBOOT|POWER\s*ON|POWER\s*OFF)", re.IGNORECASE)

with open("serial_log.log", "r", errors="ignore") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
