import win32clipboard
import time
import pyautogui as p

def wait_for_element(element):
    result = p.locateCenterOnScreen(f'./screenshots/{element}.PNG', confidence=0.9)
    while result == None:
        result = p.locateCenterOnScreen(f'./screenshots/{element}.PNG', confidence=0.9)
        time.sleep(0.5)
        print(result)
    return result

def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return value
    except:
        return 'BLANK'
    
def ctrl_1():
    p.keyDown('ctrl')
    p.press('1')
    p.keyUp('ctrl')

def copy():
    p.keyDown('ctrl')
    p.press('c')
    p.keyUp('ctrl')

def select_chrome_tab(tab_number):
    p.keyDown('ctrl')
    p.press(f"{tab_number}")
    p.keyUp('ctrl')

def select_all():
    p.keyDown('ctrl')
    p.press("a")
    p.keyUp('ctrl')

def close_tab():
    p.keyDown('ctrl')
    p.press("w")
    p.keyUp('ctrl')
    
def check_for_multiple_tabs():
    one_page = p.locateCenterOnScreen('./screenshots/one_page.PNG', confidence=0.9)
    if (one_page): return True
    else: return False