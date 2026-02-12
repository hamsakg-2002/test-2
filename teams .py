import subprocess
import pyautogui
import time

subprocess.Popen("C:\\Program Files (x86)\\DediProg\\SF Programmer\\dedipro.exe" )
time.sleep(10)
pyautogui.click(300,300 , duration = 1)
pyautogui.write("hi")
pyautogui.press("enter")