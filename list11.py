list = [2,2,3,3,4,4,5,6,78,9]
seen =[]
duplicate =[]
for num in list:
    if num in seen and num not in duplicate:
        duplicate.append(num)
    else:
        seen.append(num)
print(duplicate)