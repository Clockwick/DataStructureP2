class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DummySinglyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    def __str__(self):
        current = self.head.next
        s = ""
        while current:
            s += str(current.data) + ", "
            current = current.next
        return s[:-2]

    def append(self, items):
        new_node = Node(items)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, data):
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                break
            current = current.next

    def addHead(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert(self, data, i):
        new_node = Node(data)
        if i == 0:
            self.addHead(data)
        else:
            current = self.head.next
            for _ in range(i-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node


ll = DummySinglyLinkedList()
ll.append(1)
ll.append(2)
ll.remove(1)
print(ll)
ll.remove(2)
print(ll)
ll.append(5)
print(ll)
ll.append(5)
print(ll)
ll.remove(5)
print(ll)
ll.addHead(2)
ll.addHead(4)
ll.addHead(2)
ll.addHead(2)
ll.addHead(4)
ll.addHead(4)
print(ll)
ll.insert(6, 1)
print(ll)
ll.insert(10, 3)
print(ll)
