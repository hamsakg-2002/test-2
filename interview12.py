import subprocess

text = "Hello!\nThis text is written from Python.\nWelcome to Notepad automation."

file_path = "note.txt"

# write text to file
with open(file_path, "w") as f:
    f.write(text)

# open file in notepad
subprocess.Popen(["notepad.exe", file_path])

