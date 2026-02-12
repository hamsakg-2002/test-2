import re

pattern = re.compile(r"(ERROR|FAIL|ASSERT|PANIC)", re.IGNORECASE)

with open("serial_log.log", "r", encoding="utf-8", errors="ignore") as infile, \
     open("ustglobal.txt", "w", encoding="utf-8") as outfile:

    for line in infile:
        if pattern.search(line):
            outfile.write(line)

print("Errors written to ustglobal.txt")
