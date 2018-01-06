# O(N) runtime.

from collections import deque
import time

start_time = time.time()

def main():
    d = deque('abcdefghij')
    #kv = kVal(d, 3)   # short way. return the 3rd to last value of d. Runtime = 3.88622283936e-05 seconds
    #kv = kVal2(d, 3)   # medium way, if we're not allowed to use d[v]. Runtime = 3.91006469727e-05 seconds
    #kv = kVal3(d, 3)   # long way, if we're not allowed to use len(d). Runtime = 4.10079956055e-05 seconds
    kv = kVal4(d, 3)   #slightly shorter, not allowed to use len(d) but can reverse. Runtime = 3.981590271e-05
    print kv


def kVal(d, k):
    l = len(d)
    v = l - k
    return d[v]

def kVal2(d, k):
    l = len(d)
    v = l - k

    counter = 0

    for item in d:
        if counter == v:
            return item
        counter += 1

def kVal3(d, k):

    counter = 0
    for item in d:
        counter += 1

    v = counter - k

    counter = 0

    for item in d:
        if counter == v:
            return item
        counter += 1

def kVal4(d, k):

    counter = 1  # Since d starts at index 0, but we're talking about 3rd from last.

    for item in reversed(d):
        if counter == k:
            return item
        counter += 1

if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
