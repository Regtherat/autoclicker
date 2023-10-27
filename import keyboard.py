import pynput
import math
import time
from pynput.mouse import Button, Controller
mouse = Controller()

#type the amount of times u want it to click in the i in range area then that number is multiplied by my code 11 * 8 so it can click more
#asking how much u wanna click
print("type the number of autoclick")
clicknum = int(input())
total = clicknum + 11 * 8
print(total)
print("is the number  the number you want? if yes then it will wait three seconds then spam the click button type yes or no\n")
yesorno = input().upper()

#Where the clicking happens
if yesorno == "YES":
        time.sleep(3)
        for i in range (total):
            for i in range (11):
        
                mouse.click(Button.left, 1)
  
            for i in range (11):
        
                mouse.click(Button.left, 1)
    
            for i in range (11):
        
                mouse.click(Button.left, 1)
    
            for i in range (11):
        
                mouse.click(Button.left, 1)
        
            for i in range (11):
        
                mouse.click(Button.left, 1)
    
            for i in range (11):
        
                mouse.click(Button.left, 1)
        
            for i in range (11):
        
                mouse.click(Button.left, 1)
        
            for i in range (11):
        
                mouse.click(Button.left, 1)
else:
    print("ok have a good day")
  