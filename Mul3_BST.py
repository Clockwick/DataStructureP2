class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left is None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def compare(self, node):
        if node != None:
            self.compare(node.right)
            if node.data > k:
                node.data *= 3
            self.compare(node.left)


T = BST()
inp, k = input("Enter Input : ").split("/")
inp = list(map(int, inp.split()))
k = int(k)
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.compare(root)
T.printTree(root)
