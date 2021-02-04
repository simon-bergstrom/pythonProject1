import sys
import threading


class Arithmetic(object):

    total = 0

    def __init__(self):
        self.lock = threading.lock()
        self.local = 0

    def add(self, num1, num2):
        global total
        change += (num1 + num2)
        newTotal = total + change
        print("{} + {} = {} + {} = {}".format(num1, num2, total, change, newTotal))
        total = newTotal

    def sub(self, num1, num2):
        global total
        change += (num1 - num2)
        newTotal = total + change
        print("{} - {} = {} + {} = {}".format(num1, num2, total, change, newTotal))

    def mul(self, num1, num2):
        global total
        change += (num1 * num2)
        newTotal = total + change
        print("{} * {} = {} + {} = {}".format(num1, num2, total, change, newTotal))

def main(argv):
    print("--Part of Prac--")

    Arithmetic.add(35,7)

if __name__ == "__main__":
    main(sys.argv)





