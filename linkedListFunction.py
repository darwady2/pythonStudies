#From http://stackabuse.com/python-linked-lists/

#1: Define a single-linked list node. It should store the data, and have a
#   property for referencing the next item.

class listNode:

    # Initializes the class with properties to store the data and the next item.

    def __init__(self, data):

        # store the data
        self.data = data

        #Stores the reference to the next item. Starts out as "None"
        #and is replaced as the list is built.
        self.next = None

    # A method to compare the node value with the value of a different node.

    def hasValue(self, value):
        if self.data == value:
            return True
        else:
            return False

#2: We then make a class for a single-linked list, using the nodes defined above.

class singleLinkedList:

    # Initializes the class with a "head" and a "tail" property for instant access.
    # At first, both head and tail have the value None, as long as the list is empty.

    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
    #Adds an item at the end of the list.

        #Check to see if the item is a node; if not, convert it to one.
        if not isinstance(item, listNode):
            item = listNode(item)

        #If it's the first item, set it as the head.
        if self.head == None:
            self.head = item

        #If there's an existing item, first set the current tail to point to this new item.
        else:
            self.tail.next = item

        #Then, set the new tail as this item.
        self.tail = item

        return

    def list_length(self):
    #This counts the nodes in a linked List and returns the length.

        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

def main():
    node1 = listNode(15)
    node2 = listNode(8.2)
    node3 = listNode("Berlin")

    lister = singleLinkedList()
    lister.add_list_item(node1)
    lister.add_list_item(node2)
    lister.add_list_item(node3)
    print lister.list_length()


if __name__ == "__main__":
    main()
