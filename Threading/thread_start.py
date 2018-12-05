import threading

def thread_job():
    print("this is a new thread, number is %s"%threading.current_thread())


def main():
    thread_a = threading.Thread(target=thread_job)
    thread_a.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == "__main__":
    main()