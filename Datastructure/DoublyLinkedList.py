class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        current = self.head
        while current is not None:
            s += str(current.data) + ", "
            current = current.next
        return s[:-2]

    def revStr(self):
        s = ""
        current = self.tail
        while current is not None:
            s += str(current.data) + ", "
            current = current.prev
        return s[:-2]

    def size(self):
        s = 0
        current = self.head
        while current is not None:
            s += 1
            current = current.next
        return s

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def isEmpty(self):
        return self.size() == 0

    def addHead(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def isIn(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def search(self, data):
        if self.isIn(data):
            n = 0
            current = self.head
            while current is not None:
                if current.data == data:
                    return n
                n += 1
                current = current.next
        else:
            return -1

    def before(self, data):
        current = self.head
        if self.isIn(data):
            while current is not None:
                if current.data == data:
                    if current.prev == None:
                        return None
                    else:
                        return current.prev.data
                current = current.next
        else:
            return -1

    def after(self, data):
        current = self.head
        if self.isIn(data):
            while current is not None:
                if current.data == data:
                    if current.next == None:
                        return None
                    else:
                        return current.next.data
                current = current.next
        else:
            return -1

    def remove(self, data):
        current = self.head
        if self.isIn(data):
            current = self.head
            while current is not None:
                if current.data == data:
                    if current == self.head:
                        self.head.next.prev = None
                        self.head = self.head.next
                    elif current == self.tail:

                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        break
                current = current.next
        else:
            return -1

    def removeAll(self):
        self.head = None
        self.tail = None

    def removeHead(self):
        self.head = self.head.next
        self.head.prev = None

    def sort(self):
        temp_ll = DoublyLinkedList()
        min_ = 9999999
        while not self.isEmpty():
            min_ = 9999999
            current = self.head
            while current is not None:
                min_ = min(min_, current.data)
                current = current.next
            self.remove(min_)
            temp_ll.append(min_)
        self.head = temp_ll.head
        self.tail = temp_ll.tail


dl = DoublyLinkedList()
dl.append(3)
print(dl)
dl.append(4)
print(dl)
dl.append(8)
print(dl)
dl.addHead(10)
print(dl)
print(dl.revStr())
dl.sort()
print(dl)
print(dl.revStr())
# print(dl.isIn(1))
# print(dl.search(0))
# print(dl.before(3))
# print(dl.after(3))
# dl.remove(2)
# print(dl)
# print(dl.revStr())
