class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        ss = ""
        while current is not None:
            ss += str(current.data)
            current = current.next
        return ss

    def size(self):
        s = 0
        current = self.head
        while current is not None:
            s += 1
            current = current.next
        return s

    def append(self, data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

    def addHead(self, data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def isIn(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def before(self, data):
        current = self.head
        if current.data == data:
            return "No Node"
        else:
            while current is not None:
                if current.next.data == data:
                    return current.data
                current = current.next

    def remove(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
        else:
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next

    def removeAll(self):
        self.head = None
        self.tail = None

    def removeHead(self):
        self.head = self.head.next

    def __eq__(self, ll):
        return sorted(str(self)) == sorted(str(ll))

#        current = self.head
#        current_2 = ll.head
#        l_1 = []
#        l_2 = []
#        while current:
#            l_1.append(current.data)
#            current = current.next
#        while current_2:
#            l_2.append(current_2.data)
#            current_2 = current_2.next
#        l_1.sort()
#        l_2.sort()
#        if l_1 == l_2:
#            return True
#        else:
#            return False


l_1 = SinglyLinkedList()
l_2 = SinglyLinkedList()
l_1.append(1)
l_1.append(2)
l_1.append(3)
l_1.append(4)
l_2.append(4)
l_2.append(2)
l_2.append(1)
l_2.append(3)
print(l_1 == l_2)
