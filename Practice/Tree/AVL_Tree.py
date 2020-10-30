I = "Infix : "
Pre = "Prefix : "
Post = "Postfix : "
B = "Level order : "


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + self.findMax(root)

        balance = self.getBalance(root)

        if balance > 1 and root.left.val > key:
            return self.rightRotate(root)
        if balance < -1 and root.right.val < key:
            return self.leftRotate(root)
        if balance > 1 and root.left.val < key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and root.right.val > key:
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

    def leftRotate(self, z):
        y = z.right
        T3 = y.left

        z.right = T3
        y.left = z

        z.height = 1+self.findMax(z)
        y.height = 1+self.findMax(y)

        return y

    def rightRotate(self, z):
        y = z.left
        T2 = y.right

        z.left = T2
        y.right = z

        z.height = 1+self.findMax(z)
        y.height = 1+self.findMax(y)

        return y

    def findMax(self, obj):
        return max(self.getHeight(obj.left), self.getHeight(obj.right))

    def summation(self, root):
        if root == None:
            return 0
        return root.val + self.summation(root.left) + self.summation(root.right)

    def prefix(self, root):
        global Pre
        if root != None:
            Pre += str(root) + " "
            self.prefix(root.left)
            self.prefix(root.right)

    def postfix(self, root):
        global Post
        if root != None:
            self.postfix(root.left)
            self.postfix(root.right)
            Post += str(root) + " "

    def infix(self, root):
        global I
        if root != None:
            self.infix(root.left)
            I += str(root) + " "
            self.infix(root.right)

    def breath(self, root):
        global B
        q = []
        q.append(root)
        while q:
            current = q[0]
            B += str(current) + " "
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            q.pop(0)


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level+1)
        print("    " * level, node)
        printTree90(node.left, level+1)


inp = list(map(int, input("Enter Input : ").split()))
av = AVLTree()
root = None
for e in inp:
    root = av.insert(root, e)
    printTree90(root)
    print("=========================")
print(av.summation(root))
av.prefix(root)
print(Pre)
av.postfix(root)
print(Post)
av.infix(root)
print(I)
av.breath(root)
print(B)
