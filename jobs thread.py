import threading
import time

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # The flag used to suspend the thread
        self.__flag.set() # set to True
        self.__running = threading.Event() # ID used to stop the thread
        self.__running.set() # set running to True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait() # Returns immediately when True, blocks when False until the internal flag is True and returns
            print(time.time())
            time.sleep(1)

    def pause(self):
        self.__flag.clear() # Set to False to block the thread

    def resume(self):
        self.__flag.set() # Set to True to stop the thread from blocking

    def stop(self):
        self.__flag.set() # Resume the thread from the suspended state, if it has been suspended
        self.__running.clear() # set to False



a = Job()
a.start()
time.sleep(3)
a.pause()
time.sleep(3)
a.resume()
time.sleep(3)
a.pause()
time.sleep(2)
a.stop()
time.sleep(2)
a.start()