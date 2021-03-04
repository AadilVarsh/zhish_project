import pathlib
import pyautogui as pt
import subprocess
import time


# chrome -> search_bar -> type-in-url -> whatsapp-web -> attach -> send
# required snaps
# chrome
# chrome-search
# whatsapp-web
# whatsapp search
# whatsapp attach
# file location
# open

SLEEP_INTERVAL = 5

def msg_setup(message, phone_number):
    URL = f'https://api.whatsapp.com/send?phone={phone_number}&text={message}'
    # locating chrome
    chrome_img = pt.locateCenterOnScreen("../assets/chrome_icon.png", confidence=.7)
    pt.moveTo(chrome_img.x, chrome_img.y, duration=0.2)
    pt.leftClick()
    pt.moveTo(chrome_img.x, chrome_img.y - 60)
    pt.leftClick()

    # sleep
    time.sleep(SLEEP_INTERVAL)

    # chrome_search_bar
    chrome_search_bar_img = pt.locateCenterOnScreen("../assets/chrome_search_bar.png", confidence=.7)
    pt.moveTo(chrome_search_bar_img.x, chrome_search_bar_img.y, duration=.2)
    pt.leftClick()
    pt.typewrite(URL + '\n')


if __name__ == "__main__":
    msg_setup("hello", "917356998597")
