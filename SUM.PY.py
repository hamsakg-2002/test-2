import subprocess
import pyautogui
import timetim

# Step 1: Open Notepad
subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

# Step 2: Wait for Notepad to open
time.sleep(2)

# Step 3: Click inside Notepad (to focus)
pyautogui.click(478, 559)   # any blank area inside Notepad

# Step 4: Type text
pyautogui.write("Hello, pytest documentation.", interval=0.05)

# Step 5: New line
pyautogui.press("enter")
pyautogui.write("Automation is working!")
