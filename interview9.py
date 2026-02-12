import re

pattern = re.compile(r"(CPU|Memory|PCIe|USB)", re.IGNORECASE)

with open("serial_log.log", "r", errors="ignore") as infile, \
     open("C:\\Users\\default.DESKTOP-MOGIHTS\\Downloads\\hamsa\\regex.txt", "w") as outfile:

    for line in infile:
        if pattern.search(line):
            outfile.write(line)
            print(line.strip())
