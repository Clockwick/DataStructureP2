# singly linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = none


class linkedlist:
    def __init__(self):
        self.head = none

    def __str__(self):
        current = self.head
        strk = ""
        while current is not none:
            strk += current.data + ","
            current = current.next
        strk = strk.replace(",", "->")
        strk = strk[:-2]
        return strk

    def printlist(self):
        current = self.head
        while current is not none:
            print(current.data)
            current = current.next

    def size(self):
        size = 0
        current = self.head
        while current is not none:
            current = current.next
            size += 1
        return size

    def append(self, new_node):
        current = self.head
        if current is none:
            self.head = new_node
            return
        last = current
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, index, new_node):
        current = self.head
        start = 0
        if index == start:
            new_node.next = current
            self.head = new_node
        elif index < start or index > self.size():
            print("data cannot be added")
            return
        else:
            while start < index - 1:
                current = current.next
                start += 1
            new_node.next = current.next
            current.next = new_node
        print("index = {} and data = {}".format(index, new_node.data))


if __name__ == "__main__":
    n = input("Enter Input : ").split(",")  # 1 2,0:0,3:3
    ll_el = n[0].split()
    llist = LinkedList()

    node_arr = [Node(x) for x in ll_el]  # [Node(1),Node(2)]
    for node in node_arr:
        llist.append(node)
    if llist.size() == 0:
        print("List is empty")
    else:
        print("link list :", llist)

    for i in range(1, len(n)):
        index = int(n[i].split(":")[0])
        value = n[i].split(":")[1]
        llist.insert(index, Node(value))
        if llist.size() == 0:
            print("List is empty")
        else:
            print("link list :", llist)
