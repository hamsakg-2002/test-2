lst = [1, [2, [3, 4], 5], [6, [7, [8, 9]]]]
flat = []

def flatten(data):
    for item in data:
        if type(item) == list:
            flatten(item)
        else:
            flat.append(item)

flatten(lst)
print(flat)
