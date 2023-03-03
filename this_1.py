import pyautogui
import cv2
import time
'''
from PIL import Image
img = Image.open('point.png')
img.show()
'''
100
fishingTime = int(input("Enter in seconds how long should scan last: "))
end_time = time.time() + fishingTime
print(fishingTime)
while time.time() < end_time:
    Location =  pyautogui.locateOnScreen('point.png', confidence= 0.5)
    print(Location)
    while Location != None:
        print(Location)
        point = pyautogui.center(Location)
        clickX, clickY = point
        print(point)
        pyautogui.click(clickX, clickY)
        time.sleep(0.2)
        Location =  pyautogui.locateOnScreen('point.png', confidence= 0.5)
        if Location == None:
            time.sleep(4)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
    print("Sleep") 
    time.sleep(1)
    print("Awake")
    
