lst = [2, 3, 4, 56, 7, 8]

first = second = third = -999999

for num in lst:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second and num != first:
        third = second
        second = num
    elif num > third and num != first and num != second:
        third = num

print(third)
