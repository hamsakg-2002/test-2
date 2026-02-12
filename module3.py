import subprocess
text = "\n hello"
file_path ="note.txt"
with open(file_path ,"w") as file:
    file.write(text)
subprocess.Popen(["notepad.exe" ,file_path])

