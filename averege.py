nested_list=[10,[20,[30,40],90,80],100,200]
flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)
