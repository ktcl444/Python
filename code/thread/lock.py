# -*- encoding: utf8 -*-

import time
import threading

lock = threading.Lock() # 创建互斥锁
counter = 0 # 计数器

def hello(no):
    """线程函数"""
    
    global counter
    
    if lock.acquire(): # 请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(2) # 假装思考、敲键盘需要0.2秒钟
        counter += 1
        print('我%d是第%d个'%(counter,no))

    
    lock.release() # 千万不要忘记释放互斥锁，否则后果很严重

def demo():
    threads = list()
    for i in range(3): # 假设群里有30人，都喜欢吃苹果
        threads.append(threading.Thread(target=hello,args=(i,)))
        threads[-1].start()
    
    for t in threads:
        t.join()
    
    print('统计完毕，共有%d人'%counter)

if __name__ == '__main__':
    demo()