# import win32clipboard
import pyautogui as auto
from time import sleep
from datetime import datetime

sleep(3)
def write(txt):
    txt = txt.replace('    ', '\t')
    auto.write(txt, 0.15)

def changeSettings(dir):
    auto.hotkey('ctrl', ',')
    sleep(0.2)
    auto.write('indent')
    sleep(0.5)
    for i in range(5):
        auto.hotkey('tab')
        sleep(0.2)

    auto.hotkey('enter')
    auto.hotkey('enter')
    for i in range(4):
        auto.hotkey(dir)
        sleep(0.2)

    auto.hotkey('enter')
    auto.hotkey('ctrl', 'w')

# changeSettings('up')


fileName = 'Noob Vs Pro.py'
fileName = 'Input Inside If.py'

with open('python/'+fileName, 'r') as fp:
    fileData = fp.read()

sleep(0.2)
auto.hotkey('ctrl', 'p')
sleep(0.2)
write(fileName)
sleep(0.2)
auto.press('enter')

auto.hotkey('ctrl', 'a')
auto.press('del')
auto.hotkey('ctrl', 's')
# auto.hotkey('ctrl', 's')

sleep(3)

start = datetime.now()

write(fileData)

auto.hotkey('ctrl', 's')

sleep(1)
auto.hotkey('ctrl', 'j')
sleep(1)
write(f'python "{fileName}"')
auto.hotkey('enter')

# sleep(3)
# changeSettings('down')

end = datetime.now()

print(f'{end-start}')