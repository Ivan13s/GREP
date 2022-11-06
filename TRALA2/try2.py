import threading
x=0
def do_this():
    global dead
    print("This is our dead")
    x=0
    while True:
        x+=1
        pass

def main():

    global dead
    dead=False
    our_thread=threading.Thread(target=do_this)
    our_thread.start()
    a=input("Hit enter to die")
    print(a)
    dead=True
    print(x)


if ( __name__=="__main__"):
    main()