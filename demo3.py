#import subprocess

#subprocess.Popen(["notepad.exe"])
import subprocess
import time

subprocess.Popen(["notepad.exe"])
time.sleep(5)
print("Notepad opened 5 seconds ago")




