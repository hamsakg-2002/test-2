list =[23,4,5,7]
a=b=c =0
for num in list:
    c = b
    b = a
    a = num
print(c)