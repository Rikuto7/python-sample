import multiprocessing
import time


def main():
    for _ in range(2):
        print('start')
        p = multiprocessing.Process(target=task)
        p.start()


def task():
    time.sleep(5)
    print('ok')


if __name__ == '__main__':
    main()
