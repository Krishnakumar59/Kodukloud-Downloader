import os
from time import sleep
import pyautogui
import keyboard


#============Method====================

def code_breaker():
    keyboard.wait('ctrl+alt+x')
    os._exit(0)

def downloader():
    pyautogui.dragTo(1763,235,0.5)  # hover mouse to idm icon
    pyautogui.click(button='left',interval=0.25)
    pyautogui.click(x=1773, y=252)  # all downlaod link panel
    pyautogui.dragTo(281,86,0.5)         # drag to sort
    pyautogui.click(button='left',interval=0.50)
    # hover over checkbox and tick max size video
    pyautogui.dragTo(24,108,0.5)       # check 1080p video
    pyautogui.click(button='left',interval=0.75) 
    #click ok and download start
    pyautogui.click(x=1754,y=998)       # check ok and start download
    print("Video Download Started...")
    sleep(3)
    pyautogui.dragTo(1695,112,0.5)

def complete():
    pyautogui.click(x=1390,y=128)
    print("Next Page Loading...")
    sleep(3)


def content():
    sleep(2)
    pyautogui.click(x=1394,y=132)
    sleep(3)


def topic():
    sleep(2)
    pyautogui.click(x=748,y=337)
    sleep(3)


# ==============Driver Code====================

filepath = open('filehanding\input.txt')
# filepath = open("C:\\Users\Krish\PycharmProjects\KoduKloud\input.txt", "r")
line = filepath
sleep(5)
for i in line:
    if i == "topic\n":
        topic()
    elif i == "content\n":
        content()
    else:
        for j in range(int(i)):
            sleep(2)
            downloader()

