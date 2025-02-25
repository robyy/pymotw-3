#!/usr/bin/env python3
"""Use several threads to download enclosures from RSS feeds.
"""

#end_pymotw_header
from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data...
feed_urls = [
    'http://talkpython.fm/episodes/rss',
]


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


# Consumer
def download_enclosures(q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and exit only when
    the main thread ends.
    """
    while True:
        message('looking for the next enclosure')
        # Queue.get(block=True, timeout=None)
        # If optional args block is true and timeout is None (the default), block if necessary until an item is
        # available.
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save the downloaded file to the current directory
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()


# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),  # thread name, can access to it thru threading.current_thread().name
    )
    worker.setDaemon(True)
    worker.start()

# use feedparser lib to parse the rss feed(s) and put the enclosure URLs into
# the queue.
# Producer
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        # 'enclosures' is part of the feedparser api
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
message('*** main thread waiting')

# invoked in MainThread, so all the enclosure['url'] already put into Queue/enclosure_queue, and only unblock when all
# items in the Queue got consumed and removed(indicated by q.task_done())
enclosure_queue.join()
message('*** done')
