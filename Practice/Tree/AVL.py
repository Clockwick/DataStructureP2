class TreeNode(object):
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.height = 1

    def __str__(self):
        return str(self.key)


class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        z.left = T3
        y.right = z

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        z.right = T2
        y.left = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y


def printTreeN(root, level=0):
    if root != None:
        printTreeN(root.right, level+1)
        print('    ' * level, root)
        printTreeN(root.left, level+1)


inp = list(map(int, input("Enter Input : ").split(" ")))
a = AVLTree()
root = None
for i in inp:
    root = a.insert(root, i)
printTreeN(root)
