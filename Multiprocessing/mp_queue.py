import threading
import multiprocessing as mp
import time
from queue import Queue

import threading
import time
import copy
from queue import Queue

def job(lst,q):
    # res = sum(lst)
    res = 0
    for i in lst:
        res += i + i**2 + i**3
    q.put(res)

def multithreading(lst):
    # to substitute return
    q = Queue()

    # all threads are collected in this list
    threads = []

    for i in range(2):
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

    for _ in range(2):
        total += q.get()
    print('Multi Threads Result:', total)


def multicore(lst):
    mpq = mp.Queue()
    
    p1 = mp.Process(target=job, args=(copy.copy(lst),mpq))
    p2 = mp.Process(target=job, args=(copy.copy(lst),mpq))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    res1 = mpq.get()
    res2 = mpq.get()

    print('Multi Cores Result:',res1+res2)


def normal(lst):
    res = 0
    for i in lst:
        res += i + i**2 + i**3
    print('Normal Result:',res)

if __name__ == "__main__":
    lst = range(1000000)
    
    start_time = time.time()
    normal(range(2000000))
    print('Normal:', time.time()-start_time)
   
    start_time = time.time()
    multithreading(lst)
    print('Multithreading:', time.time()-start_time)

    start_time = time.time()
    multicore(lst)
    print('Multi Cores:', time.time()-start_time)