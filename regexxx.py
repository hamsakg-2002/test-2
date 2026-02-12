import re
text ="today date 12-21-26"
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b",text)
print(dates)