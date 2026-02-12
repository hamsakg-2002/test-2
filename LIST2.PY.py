list1 = [20,33,22,44,55,6]
list2 = [20,44,567,8,9]
common =[]
for num in list1:
    if num in list2:
        common.append(num)
print("common elements:",common)
