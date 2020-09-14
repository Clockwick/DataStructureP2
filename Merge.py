class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev
        return self

    def append(self, item):
        # Code Here
        new_node = Node(item)
        current = self.head
        if current is None:
            self.head = new_node
            new_node.prev = None
            return
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = None


def merge(l1, l2):
    current = l1.head
    while current.next:
        current = current.next
    l2 = l2.reverse()
    current.next = l2.head
    l2.prev = current
    current = l1.head
    print("Merge : ", end="")
    while current:
        print(current.data + " ", end="")
        current = current.next


l1, l2 = input("Enter Input (L1,L2) : ").split()
llist1 = LinkedList()
llist2 = LinkedList()
if l1.find("->") > 0:
    l1_list = l1.split("->")
    for i in l1_list:
        llist1.append(i)
if l2.find("->") > 0:
    l2_list = l2.split("->")
    for i in l2_list:
        llist2.append(i)
if l1.find("->") == -1:
    llist1.append(l1)
if l2.find("->") == -1:
    llist2.append(l2)
print("L1    :", l1.replace("->", " "))
print("L2    :", l2.replace("->", " "))
merge(llist1, llist2)

