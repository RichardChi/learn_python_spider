#!/usr/bin/env python
#coding=utf-8
from multiprocessing import Process, Pool, Queue
import os, time, random

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    ############################
    '''
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
    '''
    ##############################
    '''
    p = Pool(5)
    for i in range(5):
    	p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    '''
    ##############################
    
    q = Queue()
    pw = Process(target = write, args=(q,))
    time.sleep(0.5)
    pr = Process(target = read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
##############################################


from multiprocessing import Process,Queue,Pool
import multiprocessing
import os, time, random

# 写数据进程执行的代码:
def write(q,lock):
  lock.acquire() #加上锁
  for value in ['A', 'B', 'C']:
    print 'Put %s to queue...' % value		
    q.put(value)		
  lock.release() #释放锁  

# 读数据进程执行的代码:
def read(q):
  while True:
    if not q.empty():
      value = q.get(False)
      print 'Get %s from queue.' % value
      time.sleep(random.random())
    else:
      break

if __name__=='__main__':
  manager = multiprocessing.Manager()
  # 父进程创建Queue，并传给各个子进程：
  q = manager.Queue()
  lock = manager.Lock() #初始化一把锁
  p = Pool()
  pw = p.apply_async(write,args=(q,lock))	
  pr = p.apply_async(read,args=(q,))
  p.close()
  p.join()
  
  print
  print '所有数据都写入并且读完'