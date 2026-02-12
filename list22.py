list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged_list = []

for i in list1:
    if i not in merged_list:
        merged_list.append(i)

for j in list2:
    if j not in merged_list:
        merged_list.append(j)

print(merged_list)
