#引入库 threading
import threading


class Person(object):
    def __init__(self):
        print("init person")

    def speak(self):
        print("speak")


if __name__ == "__main__":
    p = Person()
    while True:
        timer = threading.Timer(5, Person.speak, (p,))
        print("start")
        timer.start()
        timer.join()
        print("after join")
