cpu_info = {
    "cpucore": "10",
    "cpuspeed": "1.4GHZ",
    "busWidth": "64bit",
    "cpuTreads": "20"
}
d={}
for k,v in cpu_info.items():
    d[v]=k
print(d)