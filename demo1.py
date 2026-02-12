import os
file_path ="C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hamsa\\regex.txt"
if os.path.exists(file_path):
    print("file exists")
else:
    print("file doesnot exists")