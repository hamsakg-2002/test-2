lst = [1, [22, [3, 14], 5], [6, [7, [8, 9]]]]

def find_max(data):
    mx = -999999
    for item in data:
        if type(item) == list:
            val = find_max(item)
            if val > mx:
                mx = val
        else:
            if item > mx:
                mx = item
    return mx

print(find_max(lst))
