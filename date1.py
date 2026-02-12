import re
import logging

with open("serial_log.log", "r", encoding="utf-8") as file:
    for line in file:
        if re.search(r'\bERROR\b.*', line):
            print(line.strip())

