import pyautogui
import time
time.sleep(10)
pyautogui.typewrite("""
from cryptography.fernet import Fernet



key = Fernet.generate_key()
print(key)


# *********************** File Encrypt ***********************

# f = Fernet(key)

# with open('aa.png', 'rb') as original_file:
#     original = original_file.read()
    

# encrypted = f.encrypt(original)

# with open ('aa.png', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)


# *********************** File Dencrypt ***********************

f = Fernet(key)

with open('aa.png', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('aa.png', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)




""",interval=0.3)