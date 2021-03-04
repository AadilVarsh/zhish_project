import pyautogui as pt
import time
from pynput.keyboard import Key, Controller
import os

# chrome -> search_bar -> type-in-url -> whatsapp-web -> attach -> send
# required snaps
# chrome
# chrome-search
# whatsapp-web
# whatsapp search
# whatsapp attach
# file location
# open

KEYBOARD = Controller()
SLEEP_INTERVAL = 5
ATTACHMENT = r"E:\study-material\img.png"
DEFAULT_ATTACHMENT = r"C:\Users\Admin\Pictures\send"


def initial_phase(message, phone_number):
    URL = f'https://api.whatsapp.com/send?phone={phone_number}&text={message}'
    # locating chrome
    chrome_img = pt.locateCenterOnScreen("../assets/browser_icon.png", confidence=.7)
    if chrome_img != None:
        pt.moveTo(chrome_img.x, chrome_img.y, duration=0.2)
        pt.leftClick()
        pt.moveTo(chrome_img.x, chrome_img.y - 60)
        pt.leftClick()

    # sleep
    time.sleep(SLEEP_INTERVAL)

    # chrome_search_bar
    chrome_search_bar_img = pt.locateCenterOnScreen("../assets/browser_search_bar.png", confidence=.7)
    if chrome_search_bar_img != None:
        pt.moveTo(chrome_search_bar_img.x, chrome_search_bar_img.y, duration=.02)
        pt.leftClick()
        pt.typewrite(URL + '\n')

    time.sleep(SLEEP_INTERVAL)

    whatsapp_continue_img = pt.locateCenterOnScreen("../assets/continue_button.png", confidence=.7)
    if whatsapp_continue_img != None:
        pt.moveTo(whatsapp_continue_img.x, whatsapp_continue_img.y, duration=.2)
        pt.leftClick()

    time.sleep(SLEEP_INTERVAL)

    web_continue_img = pt.locateCenterOnScreen("../assets/whatsapp_web_use.png", confidence=.7)
    if web_continue_img != None:
        pt.moveTo(web_continue_img.x, web_continue_img.y, duration=.2)
        pt.leftClick()

    web_login = pt.locateCenterOnScreen("../assets/wtsp_web_login.png", confidence=.7)

    time.sleep(SLEEP_INTERVAL + 2)

    if web_login is None:
        if ATTACHMENT is None:
            send_attachment(location='default')
        else:
            send_attachment(location=ATTACHMENT)

    else:
        print('LOG IN TO WHATSAPP WEB!!')
        quit()

    time.sleep(SLEEP_INTERVAL)

    final_send = pt.locateCenterOnScreen("../Assets/final_send.png", confidence = .7)

    if final_send != None :
        pt.moveTo(final_send.x, final_send.y, duration=.3)
        pt.leftClick()

    time.sleep(SLEEP_INTERVAL)

    quit()



def quit():
    close_recg = pt.locateCenterOnScreen("../assets/close_button_recog.png", confidence=.7)
    time.sleep(2)
    if close_recg != None:
        pt.moveTo(close_recg.x, close_recg.y - 30, duration=.3)
        pt.leftClick()

    final_leave = pt.locateCenterOnScreen("../assets/final_leave.png", confidence = .7)
    if final_leave != None:
        pt.moveTo(final_leave.x, final_leave.y, duration=.3)
        pt.leftClick()


def send_attachment(location):
    attach_icon = pt.locateCenterOnScreen("../assets/attachment_icon.png", confidence=.7)
    if attach_icon != None:
        pt.moveTo(attach_icon.x, attach_icon.y, duration=.2)
        pt.leftClick()
        pt.moveTo(attach_icon.x, attach_icon.y - 220, duration=.2)
        pt.leftClick()

    time.sleep(SLEEP_INTERVAL)

    open_prompt_recg = pt.locateCenterOnScreen('../assets/open_prompt_recg.png', confidence=.7)
    if open_prompt_recg != None:
        pt.moveTo(open_prompt_recg.x, open_prompt_recg.y, duration=.3)
        pt.moveTo(open_prompt_recg.x + 200, open_prompt_recg.y + 25, duration=.3)
        pt.leftClick()

        KEYBOARD.press(Key.ctrl_l)
        KEYBOARD.press('a')
        KEYBOARD.release(Key.ctrl_l)
        KEYBOARD.release('a')
    if location == 'default':
        _location = DEFAULT_ATTACHMENT
        pt.typewrite(_location + '\n')
        temp_x, temp_y = pt.position()
        pt.moveTo(temp_x, temp_y + 70)
        pt.leftClick()
        pt.typewrite('\n')

    else:
        clear_attachments()
        location = f'copy {location.replace("", "")} {os.getcwd()}\..\Attachments\\'
        os.system(location)
        location = f'{os.getcwd()}/../Attachments/'
        pt.typewrite(location.replace('/', '\\') + '\n')
        temp_x, temp_y = pt.position()
        pt.moveTo(temp_x, temp_y + 70)
        pt.leftClick()
        pt.typewrite('\n')

        # file_icon = pt.locateCenterOnScreen('../assets/wtsp_file_icon.png', confidence = .8)
        # if file_icon != None:
        #     pt.moveTo(file_icon.x, file_icon.y, duration=.2)
        #     pt.leftClick()
        # quit()


def clear_attachments():
    files = os.listdir('../Attachments/')
    os.remove('../Attachments/' + files[0])


if __name__ == "__main__":
    initial_phase("hello", "917356998597")
