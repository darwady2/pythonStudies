import linkedListFunction as ll

def main():
    node1 = ll.listNode(15)
    node2 = ll.listNode(8.2)
    node3 = ll.listNode("Berlin")

    lister = ll.singleLinkedList()
    lister.add_list_item(node1)
    lister.add_list_item(node2)
    lister.add_list_item(node3)
    print lister.list_length()


if __name__ == "__main__":
    main()
