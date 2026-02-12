lst = [2, 3, 4, 56, 7, 8]
first = second = -999999
for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)
