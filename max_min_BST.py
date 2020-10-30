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

    def __str__(self):
        return str(self.root.data)

    def min(self, node):
        if node == None:
            return 9999999999999
        res = node.data
        lnode = self.min(node.left)
        rnode = self.min(node.right)
        if lnode < res:
            res = lnode
        if rnode < res:
            res = rnode
        return res

    def max(self, node):
        if node == None:
            return 0
        res = node.data
        lnode = self.max(node.left)
        rnode = self.max(node.right)
        if lnode > res:
            res = lnode
        if rnode > res:
            res = rnode
        return res


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(f"Min : {T.min(root)}")
print(f"Max : {T.max(root)}")

