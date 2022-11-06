import time
import random
import pyautogui
import smtplib
from important import google_p
import random
from random import randint
from time import sleep

# print(pyautogui.size())

while True:
    time.sleep(3)
    x, y = pyautogui.locateCenterOnScreen("centralizatorsate.png")
    #print(x,y)
    pyautogui.moveTo(260,104, duration=0)
    #x, y = pyautogui.locateCenterOnScreen("farming villages.png")
    #print(x,y)
    pyautogui.moveTo(339,483, duration=0.003)
    pyautogui.leftClick()
    pyautogui.sleep(3)
    # x, y = pyautogui.locateCenterOnScreen("select all.png")
    # pyautogui.moveTo(768,277,duration=2)
    pyautogui.leftClick(768, 277)
    # x, y = pyautogui.locateCenterOnScreen("collect.png")
    # 1306 859
    pyautogui.leftClick(1306, 859)
    pyautogui.sleep(1)
    #x, y = pyautogui.locateCenterOnScreen("storage.png")
    # 958 570

    #x, y = pyautogui.locateCenterOnScreen("inchide.png")
    # 1187 477
    #pyautogui.leftClick(1187, 477)
    pyautogui.sleep(2)
    #x, y = pyautogui.locateCenterOnScreen("close.png")
    # 1428 225
    pyautogui.leftClick(1428, 225)
    # send_mail(
    #     email_sender="python13sd@gmail.com",
    #     email_receiver="python13sd@gmail.com",
    #     message="You have attack!",
    #     password=google_p['password'],
    #     subject="Notification"
    # )
    #
    # print("Mail sent!")

    # server=smtplib.SMTP("smtp.gmail.com",587)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    #
    # server.login("python13sd@gmail.com",google_p['password'])
    # subject="Notification"
    # body="S-a oprit botul!"
    #
    # msg= f"subject : {subject}\n\n{body}"
    #
    # server.sendmail(
    #     from_addr="python13sd@gmail.com",
    #     to_addrs="python13sd@gmail.com",
    #     msg=msg
    # )
    # print("Gataa")
    cv = randint(5, 15)
    print(cv)
    time.sleep(cv)
    print("Finish")
