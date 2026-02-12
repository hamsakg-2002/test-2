list =[2,3,4,4,5,6,7,8]
duplicate_list =[]
for item in list:
    if item not in duplicate_list:
        duplicate_list.append(item)
print(duplicate_list)