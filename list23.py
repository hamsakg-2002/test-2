list1 = [1, 2, 3]
list2 = [4, 50, 6,7]
merged_list = []
for i in list1:
  merged_list.append(i)   
for j in list2:
 merged_list.append(j)
(merged_list)

list =[1,2,3,4,50,6,7]
for i in range (len(list)):
    for j in range(len(list)-1):
        if list[j]<list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)


