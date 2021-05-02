#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Burning a candle at both ends.
"""

# end_pymotw_header
import collections
import threading
import time

candle = collections.deque(range(5))
print(candle)

# also see https://docs.python.org/3/library/queue.html#module-queue
def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()


print('----------')
def _object(name, **properties):
    print(name, properties)


_object("Car", color="Red", cost=999999, company="Ferrari")


print('-----------')
def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())

# args could be list or tuple, if use tuple and target method only has one parameter, need to put extra ',' like args=(2,), or args=(2) is
# not a tuple
t1 = threading.Thread(target=thread_delay, args=['t1', 1])
t2 = threading.Thread(target=thread_delay, args=('t2', 3))

t1.start()
t2.start()

# blocks calling thread(main thread here) until the thread whose join() method is called terminates -- either normally or through an
# unhandled exception or until the optional timeout occurs.
t1.join()
# t2.join()

print("Thread execution is complete!")

# concurrency - threading, multiple threads running in one cpu core, cpu clock resource dispatched between threads,
# but only one thread running at a time. For multiple cpu cores machine, multiple threads can be executed at the same time.

# parallelism - multiple cpu cores, tasks/processes can be run/executed at the exact same time.

# https://www.datacamp.com/community/tutorials/python-global-interpreter-lock
# In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once no matter how many cpu cores
# you have(even though certain performance-oriented libraries might overcome this limitation). If you want your application to
# make better use of the computational resources of multi-core machines, you are advised to use multiprocessing or
# concurrent.futures.ProcessPoolExecutor. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks
# simultaneously.
# However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing
# computationally-intensive tasks such as compression or hashing. Also, *the GIL is always released when doing I/O*.

# Use multi threads for I/O bound tasks, use multi processing for CPU bound tasks.
