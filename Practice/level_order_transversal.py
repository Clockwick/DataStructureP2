class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = Node(key)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key)
                        break
                    else:
                        current = current.right
            return self.root

    def printTreeN(self, node, level=0):
        if node != None:
            self.printTreeN(node.right, level+1)
            print("    " * level, node)
            self.printTreeN(node.left, level+1)

    def fifo(self, root):
        q = []
        if root is None:
            return
        q.append(root)
        while q:
            current = q[0]
            print(str(current.key)+", ", end="")
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            q.pop(0)


T = BST()
inp = [int(i) for i in input("Enter Input : ").split(" ")]
print(inp)
for i in inp:
    root = T.insert(i)
T.printTreeN(root)
print("FIFO : ", end="")
T.fifo(root)
