# Singly Linked List
class Node:
    def __init__(self, data, pos=0):
        self.data = data
        self.next = None
        self.pos = pos


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def index(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.pos
            else:
                current = current.next
        print("Items not present in list")

    def atBegin(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def atEnd(self, new_node):
        current = self.head
        if current is None:
            current = new_node
            return
        last = current
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, index, new_node):
        current = self.head
        start = 0
        while start < index:
            current = current.next
            start += 1
        new_node.next = current.next
        current.next = new_node

    def remove(self, node):
        current = self.head
        while current is not node:
            current = current.next
    # Remove


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    llist.head.next = second
    second.next = third

    llist.atBegin(fourth)
    llist.atEnd(fifth)
    llist.insert(1, sixth)
    llist.printList()
