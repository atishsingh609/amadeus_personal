"""
https://realpython.com/intro-to-python-threading/


"""




import threading
import logging
import time


def logging_running_thread(start: int, end:int, name):
    with threading.Lock():
        for i in range(start, end):
            print(f" Thread starting {name} :: count is {i}", end="\n")
            time.sleep(1)

if __name__ == "__main__":
    threads = []
    for i in range(10):
        thread_1 = threading.Thread(target=logging_running_thread, args=(10,20, i))
        threads.append(thread_1)
        thread_1.start()

    # for thread in threads:
    #     thread.join()





