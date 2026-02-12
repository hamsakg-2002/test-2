import re

pattern = re.compile(r"(ERROR|FAIL|ASSERT|PANIC|SEC|PEI|DXE|BDS)", re.IGNORECASE)

with open("serial_log.log", "r", errors="ignore") as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())
