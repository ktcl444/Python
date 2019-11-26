# -*- encoding: utf8 -*-

import time
import threading

locks = list()
hammer_users = dict()

def init_locks(i):
    for j in range(i):
        hammer_no = j+1
        print('初始化%d号锁'%hammer_no)
        lock = threading.Lock()
        locks.append(lock)

def us_hammer(id,hammer_num):
    work_no = id +1
    for i in range(hammer_num):
        lock = locks[i]
        hammer_no = i+1
        print('%d号工人来借%d号电锤'%(work_no,hammer_no))
        if lock.locked():
            print('%d号工人正在使用%d号电锤'%(hammer_users[hammer_no],hammer_no))
        else:
            lock.acquire()
            print('%d号工人借走了%d号电锤'%(work_no,hammer_no))
            hammer_users[hammer_no] = work_no
            time.sleep(2)
            lock.release()
            print('%d号工人归还了%d号电锤'%(work_no,hammer_no))
            break
 
def demo():
    hammer_num = 3
    worker_num = 5
    init_locks(hammer_num)
    print('初始化锁结束')
    threads = list()
    for i in range(worker_num): 
        threads.append(threading.Thread(target=us_hammer, args=(i,hammer_num)))
        threads[-1].start()
        threads[-1].join(1)    

if __name__ == '__main__':
    demo()