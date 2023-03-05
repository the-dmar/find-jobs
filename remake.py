import pyautogui as p
import time
import re
from utils.utils import get_clipboard_data, wait_for_element, ctrl_1, copy, select_chrome_tab, select_all, close_tab, check_for_multiple_tabs

def main():
    stop = False
    while stop == False:
        one_page = check_for_multiple_tabs()
        if one_page == False:
            select_chrome_tab(2)
            close_tab()
            select_chrome_tab(1)
            
        dots_on_screen = p.locateAllOnScreen('./screenshots/dots.PNG', confidence=0.9)
        for dots in dots_on_screen:
            p.click(dots[0] - 350, dots[1], button = 'middle') # open listing in a new tab
            time.sleep(1)
            job_description = get_job_description()
            time.sleep(2)
            eligible = check_if_eligible(job_description)
            time.sleep(2)
            if eligible:
                heart = p.locateCenterOnScreen('./screenshots/heart.PNG', confidence=0.9)
                if (heart): p.click(heart)
                time.sleep(2)
            close_tab()
            time.sleep(5)
            
        next_page = p.locateCenterOnScreen('./screenshots/next_page.PNG', confidence=0.9)
        if (next_page):
            p.click(next_page)
            wait_for_element('dots')
            ctrl_1()
        else: 
            p.press('pagedown')
            ctrl_1()
                
            
def get_job_description():
    select_chrome_tab(2)
    select_all()
    copy()
    job_description = get_clipboard_data()
    return job_description

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
        'Comptia',
        'java\W',
        'sr\W',
        'wordpress',
        'android',
        'ios',
        '\.net',
        'mariadb',
        'apache',
        'angular'
        'vue',
        'ruby on rails',
        'jira',
    ]

    search = '|'.join(exclusions)
    print(f"({search})")

    result = re.findall(f"({search})", job_description.lower())
    print(result)
    if (len(result) == 0):
        print('ELIGIBLE!')
        return True
    else: return False

            
main()