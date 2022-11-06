import random
import threading
import time

import pyautogui


def run(stop):
    CEVA = random.uniform(4, 10)
    time.sleep(CEVA)
    print(CEVA)
    pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
    pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
    print("finish")
    time.sleep(2)
    while True:
        global stop_threads
        CEVA = random.uniform(0, 3)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
        print("finish")
        time.sleep(1)
        print("abcd")
        if stop():
            print("abcd2")
            break


def main():
    stop_threads = False
    t1 = threading.Thread(target=run, args=(lambda: stop_threads,))
    t1.start()

    stop_threads = True
    t1.join()

    print('thread killed')


main()
