# A deque is a double-ended queue, or double-linked list.
# The underlying data structure of deque is a Python list which is double-linked.
# The first list node has the index 0.
# From this tutorial: https://pymotw.com/2/collections/deque.html

"""
Deque Methods:
append(): add an item to the right side of the list (end)
append_left(): add an item to the left side of the list (head)
clear(): remove all items from the list
count(): count the number of items with a certain value
index(): find the first occurrence of a value in the list
insert(): insert an item in the list
pop(): remove an item from the right side of a list (end)
popleft(): remove an item from the left side of a list (head)
remove(): remove an item from the list
reverse(): reverse the list
"""

from collections import deque

def createD(value):
    d = deque(value)
    print 'Deque: ', d
    print 'Length:', len(d)
    print 'Left End:', d[0]
    print 'Right End:', d[-1]

    d.remove(d[2])
    print 'Removed 3rd value:', d

    return d



def main():
    createD('abcdefg')






if __name__ == "__main__":
    main()
