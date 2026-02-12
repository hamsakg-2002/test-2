input_str = "aabbccddaadd"

result = []
count = 1

for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]:
        count += 1
    else:
        result.append(str(count))
        result.append(input_str[i - 1])
        count = 1

# append last character group
result.append(str(count))
result.append(input_str[-1])

output = "".join(result)
print(output)
