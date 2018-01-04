#From http://stackabuse.com/python-linked-lists/

#1: Define what a singly-linked linkedList node is. It should store the data, and
#   have a space for referencing the next item.

class ListNode(self, data):
    def __init__(self, data):

        # store the data
        self.data = data

        # store the reference to the next item.
        self.next = None

    def hasValue(self, value):
        if self.data == value:
            return True
        else:
            return False
