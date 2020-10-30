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

    def printTree90(self, node, level=0):
        if node != None:
            self.printTree90(node.right, level+1)
            print('    ' * level, node)
            self.printTree90(node.left, level+1)


T = BST()
inp = list(map(int, input("Enter Input : ").split()))
for e in inp:
    root = T.insert(e)

T.printTree90(root)
