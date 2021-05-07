#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""PriorityQueue
"""

#end_pymotw_header
import functools
import queue
import threading


@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        # return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


# binary heap
q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()  # without task_done(), main thread will never reach the code after q.join()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    # https://stackoverflow.com/questions/5127401/setdaemon-method-of-threading-thread

    # Basically there are two types of thread. One is daemon thread. Another is non-daemon thread.
    #
    # While a non-daemon thread blocks the main program to exit if they are not dead. A daemon thread runs without blocking the
    # main program from exiting. And when main program exits, associated daemon threads are killed too.
    # https://cppsecrets.com/users/11611181181051069712197495764103109971051084699111109/Python-threading-setDaemon.php
    w.setDaemon(True)  # notice that there's a while True in process_job(q)
    w.start()

# Queue.join() Blocks until all items in the queue have been gotten and processed.
#
# The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer thread calls
# task_done() to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero,
# join() unblocks.
q.join()

print('after q.join()')
