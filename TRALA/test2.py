import threading
import time


def run(stop):
    while True:
        print('thread running')
        if stop():
            break


def main():
    stop_threads = False
    t1 = threading.Thread(target=run, args=(lambda: stop_threads,))
    t1.start()
    stop_threads = True
    t1.join()
    print('thread killed')


main()