class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

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

    def isEmpty(self):
        return self.head == None

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

    def addHead(self, item):
        # Code Here
        new_node = Node(item)
        current = self.head
        if current is None:
            self.append(item)
            return
        current.prev = new_node
        new_node.next = current
        self.head = new_node
        new_node.prev = None

    def insert(self, pos, item):
        # Code Here
        current = self.head
        new_node = Node(item)
        start = 0
        if current is None:
            self.append(item)
            return
        if pos == start:
            new_node.next = current
            new_node.prev = None
            self.head = new_node

        elif pos <= -(self.size()):
            self.addHead(item)

        elif pos < start:
            self.insert(self.size() + pos, item)

        elif pos > self.size():
            self.append(item)
        else:
            while start < pos - 1:
                current = current.next
                start += 1
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node

    def search(self, item):
        # Code Here
        if self.index(item) != -1:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        # Code Here
        new_node = Node(item)
        current = self.head
        index = 0
        while current.data != item and current.next:
            current = current.next
            index += 1

        if current.data == item:
            return index
        return -1

    def size(self):
        # Code Here
        current = self.head
        size = 0
        if current is None:
            return size
        else:
            while current:
                current = current.next
                size += 1
        return size

    def pop(self, pos):
        if pos < 0 or pos > self.size()-1 or self.isEmpty():
            return "Out of Range"

        current = self.head
        for _ in range(pos):
            current = current.next
        if current.next is None:
            current = None
            self.head = self.head.prev

        elif current.next is not None:
            current.prev.next = current.next
            current.next.prev = current.prev

        return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
