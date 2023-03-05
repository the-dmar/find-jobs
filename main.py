import pyautogui as p
import time
import re
from utils.utils import get_clipboard_data, wait_for_element, ctrl_1, copy


def main():
    stop = False
    while stop == False:
        dots_on_screen = p.locateAllOnScreen('./screenshots/dots.PNG', confidence=0.9)
        for dots in dots_on_screen:
            p.click(dots[0] - 200, dots[1])
            job_description = get_description()
            eligible = check_if_eligible(job_description)
            if (eligible):
                print('ELIGIBLE!')
                heart = p.locateCenterOnScreen('./screenshots/heart.PNG')
                if (heart): p.click(heart)

        next_page = p.locateCenterOnScreen('./screenshots/next_page.PNG', confidence=0.9)
        if (next_page):
            p.click(next_page)
            wait_for_element('dots')
            ctrl_1()
        else: 
            p.press('pagedown')
            ctrl_1()

    
def check_if_eligible(job_description):
    exclusions = [
        'c\+\+',
        'c#',
        'springboot'
        'part time',
        'bachelor',
        '5\+',
        '6\+',
        '7\+',
        '8\+',
        'senior',
        'CompTIA',
        'java\W',
        'sr\W'
    ]

    search = '|'.join(exclusions)
    print(f"({search})")

    result = re.findall(f"({search})", job_description.lower())
    print(result)
    if (len(result) == 0): return True
    else: return False
    

main()