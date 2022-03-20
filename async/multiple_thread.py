import threading
import time


def main():
    for _ in range(5):
        print('start')
        t = threading.Thread(target=task)
        t.start()


def task():
    time.sleep(5)
    print('ok')


if __name__ == '__main__':
    main()
