#import re
#text = "python is a coding language , I learnt python in 10 days ,python is not a object oriented program"
#pattern = r'\bpython\b'
#matches = re.findall(pattern, text, flags=re.IGNORECASE)
#count = len(matches)
#print(count)
#print(f"'python' appears {count} times")

#import re
#text = "0011:0022:003"
# Regex pattern to remove leading zeros
# \b0+ matches one or more zeros at the start of a word boundary
#result = re.sub(r'\b0+(\d+)', r'\1', text)
#print(result)

#import re
#text = "You can contact me at 9876543210 or 012-345-6789, or +91 98765-43210."
#text = "you can contact me at 8867740877"
# Regex pattern to match phone numbers (no capturing groups)
#pattern = r'\+?\d{1,3}[-\s]?\(?\d{2,3}\)?[-\s]?\d{3,5}[-\s]?\d{4}'
## Find all matches
#phone_numbers = re.findall(pattern, text)
#print("Phone numbers found:")
#print(phone_numbers)

#import re
#text = """
#Contact us at john.doe@example.com, support@sub.domain.co.in,
#user_name-123@domain.org, or first.last+tag@company-mail.com
"""# Regex pattern to match most valid email addresses
#pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# Find all matches
#matches = re.findall(pattern, text)
#print("Email IDs found:")
#print(matches)

