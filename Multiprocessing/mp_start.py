import multiprocessing as mp

def job():
    print('aaaaa')


if __name__ == '__main__':
    # only run in main
    p1 = mp.Process(target=job)
    p1.start()
    p1.join()