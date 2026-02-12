d = {'a': 10, 'b': 5, 'c': 20}
min_key = None
min_val = None
for k in d:
    if d[k] < min_val:
       min_val = d[k]
       min_val = k
print(min_val)