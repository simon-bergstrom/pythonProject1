import threading
import time

# Function to create thread
lock = threading.Lock()
count = 0

def incrementor():
    global count
    while(1):
        lock.acquire()
        try:
            count += 1
            print('incrementor: ', count)
        finally:
            lock.release()
            time.sleep(1)



def decrementor():
    global count
    while(1):
        lock.acquire()
        try:
            count -= 1
            print('decrementor: ', count)
        finally:
            lock.release()
            time.sleep(5)


t = threading.Thread(name='incrementor', target=incrementor)
w = threading.Thread(name='decrementor', target=decrementor)

t.start()
w.start()