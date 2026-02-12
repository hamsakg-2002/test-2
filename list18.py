dict = {
    "cpucore": "10",
    "cpuspeed": "1.4GHZ",
    "busWidth": "64bit",
    "cpuTreads": "20"
}

reversed_dict = {}
for key in dict:
    reversed_dict[dict[key]] = key

print(reversed_dict)

