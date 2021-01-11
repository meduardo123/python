import pyautogui
import time
import clipboard

pyautogui.hotkey('alt', 'tab')
pyautogui.click(389, 355)
pyautogui.doubleClick(389, 355)
pyautogui.hotkey('ctrl', 'c')
os=clipboard.paste()
if os == '001 ':
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.write('1')
    pyautogui.hotkey('enter')
elif not os.isspace():
    print(os)
    print('fechar os?')
else: 
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('alt', 'tab')

