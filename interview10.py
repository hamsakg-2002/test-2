#import os
#file_path=("C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hamsa\\regex.txt")
#if os.path.exists(file_path):
    #print("file exists")
#else:
    #print("file doesnt exists")

import os
file_path =("C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hamsa\\regex.txt")
with open(file_path ,"a") as f:
    f.write("\n name:hamsa , age :24")
print("content appended succesfully")