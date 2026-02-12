#import pyautogui
#import time
#print("move mouse to the button in 10sec ")
#time.sleep(10)
#print(pyautogui.position())
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
