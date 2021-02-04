import sys
import threading
import time

def demo():
    print("DEMO")

def incrementor(num):
    for i in range(10):
        print(num)
        num += 1

def decrementor(num):
    for i in range(10):
        print(num)
        num -= 1

def main(argv):
    print("--Part 1 of Prac ---")
    threadInc = threading.Thread(target=incrementor, args=(42,))
    threadDec = threading.Thread(target=decrementor, args=(42,))

    threadInc.start()
    threadDec.start()

    threadInc.join()
    threadDec.join()

    print("done ...")

if __name__ == "__main__":
    main(sys.argv)