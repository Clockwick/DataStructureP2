class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.dir = ""
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        self.dir += "R"
                        break
                    else:
                        self.dir += "R"
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(data)
                        self.dir += "L"
                        break
                    else:
                        self.dir += "L"
                        current = current.left
            print(self.dir + "*")
            self.dir = ""
        return self.root


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
print("*")
for i in inp:
    root = T.insert(i)
