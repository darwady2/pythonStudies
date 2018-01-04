#From http://stackabuse.com/python-linked-lists/
# To use Python's deque feature (which is a module for double-ended queues),
# see documentation in Step 7 of the article above. The below creates a linked
# list from scratch.

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

    def output_list(self):
        #Start at the top of the list.
        current_node = self.head

        #Cycle through the list, print the data, and use .next to go to the next one.
        while current_node is not None:
            print(current_node.data)

            current_node = current_node.next

        return

    def unordered_search(self, value):
        # Return a numerical list of nodes that correspond to the search.

        # Start at the head.
        current_node = self.head

        # Create the data structure to store the results.
        nodeID = 1
        results = []

        # Iterate through.
        while current_node is not None:
            if current_node.hasValue(value):
                results.append(nodeID)

            current_node = current_node.next

            nodeID += 1

        return results

    def remove_list_item_by_id(self, item_id):

        # Sets the reference from the previous node to point to the
        # remaining next node. Python automatically takes out unreferenced
        # items, so there is no need to "delete" it after adjusting the reference.

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                #If this isn't the first value:
                if previous_node is not None:
                    # Set the previous node to point to the remaining next node.
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return

            previous_node = current_node
            current_node = current_node.next
            current_id += 1
        return


def main():
    node1 = listNode(15)
    node2 = listNode(8.2)
    item3 = "Berlin"
    node4 = listNode(15)

    lister = singleLinkedList()

    for current_item in [node1, node2, item3, node4]:
        lister.add_list_item(current_item)

    print(lister.unordered_search(15))


if __name__ == "__main__":
    main()
