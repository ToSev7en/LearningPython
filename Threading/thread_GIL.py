import threading
import time
import copy
from queue import Queue

def job(lst,q):
    res = sum(lst)
    q.put(res)

def multithreading(lst):
    # to substitute return
    q = Queue()

    # all threads are collected in this list
    threads = []

    for i in range(4):
        # target is a function name alone, not a string function name in "" or '' 
        t = threading.Thread(target=job, args=(copy.copy(lst),q))
        
        # start this thread
        t.start()

        threads.append(t)

    # for thread in threads:
    #     # join the main thread
    #     thread.join()

    [t.join() for t in threads]
    
    total = 0

    for _ in range(4):
        total += q.get()
    print(total)

def normal(lst):
    total = sum(lst)
    print(total)

if __name__ == "__main__":
    lst = list(range(10000000))
    start_time = time.time()
    normal(lst*4)
    print('Normal:', time.time()-start_time)
    start_time = time.time()
    multithreading(lst)
    print('Multithreading:', time.time()-start_time)
