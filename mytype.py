import pyautogui
import time
time.sleep(15)
pyautogui.typewrite(
"""
import random,math # import modules

digits = "0123456789"  # create variable and store value
OTP = "" # create null variable 
for i in range(4) : # for loop for generate otp
OTP += digits[math.floor(random.random() * 10)] # generate otp
print(OTP) # print otp

"""
,interval=0.1)