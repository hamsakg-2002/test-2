import re
age = re.findall(r'"age"\s*:\s*(\d+)',text)
email = re.findall(r'"email"\s*:\s*"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"', text)
name = re.findall(r'"name"\s*:\s*"([^"]+)"', text)
phones = re.findall(r'"phone"\s*:\s*"(\+?\d{1,3}[- ]?\d{10})"', text)
places = re.findall(r'\b[A-Za-z]+(?:[ -][A-Za-z]+)*\b', text)
experience = re.findall(r'"experience"\s*:\s*(\d+)', text)
year_of_passing = re.findall(r'"year_of_passing"\s*:\s*(\d{4})', text)
pattern = r'"name"\s*:\s*"([^"]+)"\s*,\s*"email"\s*:\s*"([^"]+)"'
pattern = r'"name"\s*:\s*"([^"]+)"\s*,\s*"phone"\s*:\s*"([^"]+)"'
end_time =r'"([0-2]?\d:[0-5]\d)"'
name_pattern = r'"name"\s*:\s*"([^"]+)"'
date_pattern = r'"date"\s*:\s*"(\d{2}/\d{2}/\d{4})"'
dict_output = {name: int(age) for name, age in matches}
print(dict_output)

tuple_output = tuple(re.findall(pattern, text))
print(tuple_output)

list_output = re.findall(pattern, text)
print(list_output)

date_of_birth = re.findall(r'"date_of_birth"\s*:\s*"(\d{2}-\d{2}-\d{4})"', text)
pincode = re.findall(r'"(pincode|zipcode)"\s*:\s*(\d{5,6})', text)

result = re.findall(pattern, text)
result_dict = {name: int(age) for name, age in result}
print(result_dict)

