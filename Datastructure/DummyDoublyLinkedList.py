class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DummyDoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def __str__(self):
        s = ""
        current = self.head.next
        while current:
            s += str(current.data) + ", "
            current = current.next
        return s[:-2]

    def size(self):
        s = 0
        current = self.head.next
        while current:
            s += 1
            current = current.next
        return s

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Prev ", self.head.data)
        print("Next : " + str(self.head.next.data))

    def addHead(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node
        print("Prev ", self.head.data)
        print("Next : " + str(self.head.next.data))

    def isEmpty(self):
        return self.size == 0

    def remove(self, data):
        current = self.head.next
        while current:
            print("Prev ", current.prev.data)
            print("Current ", current.data)
            print("Next : " + str(self.head.next.data))
            print("Remove")
            if current.data == data:
                print(current.next.data)
                current.prev.next = current.next
                current.next.prev = current.prev
                break
            current = current.next

    def pop(self, i):
        pass

    def search(self, data):
        pass

    def index(self, i):
        pass


ll = DummyDoublyLinkedList()
ll.append(1)
ll.append(4)
ll.append(3)
ll.append(2)
print(ll)
ll.addHead(7)
ll.addHead(8)
print(ll)
ll.remove(1)
print(ll)
