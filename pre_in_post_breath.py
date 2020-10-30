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

    def pre_order(self, node):
        if node != None:
            print(str(node), end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node != None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(str(node), end=" ")

    def in_order(self, node):
        if node != None:
            self.in_order(node.left)
            print(str(node), end=" ")
            self.in_order(node.right)

    def levelOrder(self, root):
        for i in range(1, self.height(root)+1):
            self.bfs(root, i)

    def bfs(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.bfs(root.left, level-1)
            self.bfs(root.right, level-1)

    def height(self, node, level=0):
        if node != None:
            lh = self.height(node.right, level + 1)
            rh = self.height(node.left, level + 1)
            if lh > rh:
                level = lh
            else:
                level = rh
        return level

    def fifo(self, root):
        q = []
        q.append(root)
        while q:
            current = q[0]
            print(str(current) + ", ", end="")
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            q.pop(0)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("==================================")
print("Preorder : ", end="")
T.pre_order(root)
print("\nInorder : ", end="")
T.in_order(root)
print("\nPostorder : ", end="")
T.post_order(root)
print("\nBreadth : ", end="")
T.levelOrder(root)
print("\nFIFO : ", end="")
T.fifo(root)

