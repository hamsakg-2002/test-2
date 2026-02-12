num = [2, 5, 44, 6, 7, 8, 3, 4]

for i in range(len(num)):
    for j in range(len(num) - 1):
        if num[j] < num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print(num)

