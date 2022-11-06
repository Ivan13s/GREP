import time
import random
import pyautogui
time.sleep(3)
while True:
    pyautogui.leftClick(795, 317,interval=random.uniform(0.2,0.9),duration=random.uniform(0.2,0.9))
    pyautogui.leftClick(1285, 833,interval=random.uniform(0.2,0.9),duration=random.uniform(0.2,0.9))
    CEVA=random.uniform(0,30)
    ALTCEVA=int(CEVA)
    print("Altceva,fara if:",ALTCEVA)
    if ALTCEVA in range(600,900):
        pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        CEVA1=random.uniform(ALTCEVA,900)
        ALTCEVA1=int(CEVA1)
        print("Primul if ALTCEVA1:",ALTCEVA1)
        time.sleep(ALTCEVA1)
        if ALTCEVA1 in range(600,700):
            pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
            pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
            CEVA2=random.uniform(ALTCEVA1,800)
            ALTCEVA2=int(CEVA2)
            print("Al doilea if ALTCEVA2:", ALTCEVA2)
            time.sleep(ALTCEVA2)
            if ALTCEVA2 in range(800,900):
                pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
                pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
                CEVA3 = random.uniform(ALTCEVA2, 30)
                ALTCEVA3=int(CEVA3)
                print("Al treilea if ALTCEVA3:", ALTCEVA3)
                time.sleep(ALTCEVA3)



