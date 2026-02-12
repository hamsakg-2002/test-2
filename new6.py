import re

with open(r"C:\Users\default.DESKTOP-MOGIHTS\Downloads\swathi_test.json", "r") as file:
    text = file.read()

# Extract each user block
users = re.findall(
    r'\{[^{}]*"name"\s*:\s*"[^"]+"[^{}]*"age"\s*:\s*\d+[^{}]*"email"\s*:\s*"[^"]+"[^{}]*"phone"\s*:\s*"[^"]+"[^{}]*\}',
    text
)

# Print each user
for user in users:
    print(user)
    print("-" * 40)
