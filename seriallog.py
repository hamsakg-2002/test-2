import re

pattern = re.compile(r".*(ERROR|FAIL|ASSERT|PANIC).*", re.IGNORECASE)

with open("serial_log.log", "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
