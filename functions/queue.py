"""
Operations for queues in Python:

put(item): Add an item to the back of the queue.
get(): Gets an item from the front of the queue.
remove(): Remove the first item in the list (the next person at the counter)
empty(): Return true if the queue is empty
task_done(): This tells that we're done with the Queue, which is needed for threading.

"""
from Queue import Queue

def main():
    q = Queue(maxsize = 0)   # When you create a queue, you determine its size. 0 = infinite.

    for x in range(20):
        q.put(x)

    do_stuff(q)

def do_stuff(q):
    while not q.empty():
        print q.get()   # Prints 0-19 in order, since that's how they lined up in the queue.
        q.task_done   #   This is used for threading.

if __name__ == "__main__":
    main()
