import threading
import time
from queue import Queue

def job(lst,q):
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    # return lst
    q.put(lst)

def multithreading():
    # to substitute return
    q = Queue()

    # all threads are collected in this list
    threads = []

    data = [[1,2,3], [3,4,5], [4,5,6], [6,7,8]]

    for i in range(4):
        # target is a function name alone, not a string function name in "" or '' 
        t = threading.Thread(target=job, args=(data[i],q))
        
        # start this thread
        t.start()

        threads.append(t)

    for thread in threads:
        # join the main thread
        thread.join()
    
    results = []

    
    for _ in range(4):
        # access q value
        results.append(q.get())
    
    print(results)



if __name__ == "__main__":
    multithreading()
