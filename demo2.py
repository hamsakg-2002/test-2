import os
folder_path =("C:\\Users\\default.DESKTOP-MOGIHTS\\Documents\\hema")
if os.path.exists(folder_path):
    os.makedirs(folder_path,exit_ok = True)
print("folder created successfully")



