class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        show_str = ""
        current = self.tail
        while current:
            show_str += current.data + " "
            current = current.next
        return show_str

    def append(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.head.next = new_node
            self.afterAppend(new_node)
            self.head = new_node

    def afterAppend(self, new_node):
        current = self.tail
        while current:
            if current.data == "|":
                self.swap(current, new_node)
                temp = current.next
                while temp:
                    self.swap(temp, temp.next)
                    temp = temp.next
#                print("After :", self)
                break
            else:
                current = current.next

    def swap(self, a, b):
        if a is not None and b is not None:
            a.data, b.data = b.data, a.data

    def index(self, item):
        new_node = Node(item)
        index = 0
        current = self.head
        while current.next and current.data != item:
            current = current.next
            index += 1
        if current.data == item:
            return index
        return -1

    def walkBack(self):
        # swap with left node
        current = self.tail
        try:
            while current:
                if current.next.data == "|":
                    self.swap(current, current.next)
                    break
                else:
                    current = current.next
        except:
            pass

    def walk(self):
        # swap with right node
        current = self.tail
        try:
            while current:
                if current.data == "|":
                    self.swap(current, current.next)
                    break
                else:
                    current = current.next
        except:
            pass

    def removeRight(self):
        current = self.tail
        try:
            while current:
                if current.next.next and current.data == "|":
                    current.next = current.next.next
                    break
                elif current.data == "|":
                    self.head = current
                    current.next = None
                    break
                else:
                    current = current.next
        except:
            pass

    def removeLeft(self):
        current = self.tail
        try:
            while current:
                if current.next.next and current.next.next.data == "|":
                    current.next = current.next.next
                    break
                elif current.next.data == "|":
                    self.tail = current.next
                    break
                else:
                    current = current.next
        except:
            pass


if __name__ == "__main__":
    n = input("Enter Input : ").split(",")
    ll = LinkedList()
    ll.append("|")
    for i in range(len(n)):
        cmd = n[i].split()
        if cmd[0] == "I":
            ll.append(cmd[1])
        elif cmd[0] == "L":
            ll.walkBack()
        elif cmd[0] == "R":
            ll.walk()
        elif cmd[0] == "B":
            ll.removeLeft()
        elif cmd[0] == "D":
            ll.removeRight()
    print(ll)
