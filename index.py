import pyautogui as pa
import time as t
pa.FAILSAFE = False
cord = pa.locateAllOnScreen(r"C:\Users\netfl\Pictures\Screenshots\allow.png", confidence=0.8)
print(cord)

if cord is not None:
        for c in cord:
            pa.moveTo(c, duration=0.1)
            t.sleep(0.1)
            pa.click()
pa.moveTo(1500, 0, duration=0.1)
print("Clicked on all allow buttons")
