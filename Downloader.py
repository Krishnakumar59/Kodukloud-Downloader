import keyboard
import webbrowser
from time import sleep
import mouse
from playsound import playsound
import pyautogui


# ============CLASS ====================

def downloader():
    pyautogui.dragTo(1763,235,0.5)  # hover mouse to idm icon
    pyautogui.click(button='left',interval=0.25)
    pyautogui.click(x=1773, y=252)  # all downlaod link panel
    pyautogui.dragTo(281,86,0.5)         # drag to sort
    pyautogui.click(button='left',interval=0.25)
    # hover over checkbox and tick max size video
    pyautogui.dragTo(24,108,0.5)       # check 1080p video
    pyautogui.click(button='left',interval=0.25) 
    #click ok and download start
    pyautogui.click(x=1754,y=998)       # check ok and start download
    print("Video Download Started...")
    sleep(2)


def complete():
    pyautogui.click(x=1390,y=128)
    # pyautogui.click(button='left')
    print("Next Page Loading...")
    sleep(3)




while True:
    keyboard.wait('ctrl+alt+d')
    downloader()
    sleep(1)
    complete()
    sleep(3)
    print('space was pressed! Waiting on it again...')
