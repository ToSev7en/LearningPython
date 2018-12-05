import threading
import time

def thread_job_t1():
    print("T1 start \n")
    for i in range(10):
        time.sleep(0.1*i)
    print("T1 stop \n")


def thread_job_t2():
    print("T2 start \n")
    print("T2 stop \n")


def main():
    thread_t1 = threading.Thread(target=thread_job_t1, name='T1')
    thread_t2 = threading.Thread(target=thread_job_t2, name='T2')

    thread_t1.start()
    thread_t2.start()

    thread_t1.join()
    thread_t2.join()

    print("All Done \n")
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__ == "__main__":
    main()