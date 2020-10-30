op = ['+', '-', '*', '/']


def isOperator(data):
    if data in op:
        return True
    else:
        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


preset = "Infix : "


class BST:
    def __init__(self):
        self.root = None
        self.stack = []

    def insert(self, data):
        new_node = Node(data)
        if isOperator(data) and self.stack:
            self.stack.append(new_node)
            op = self.stack.pop()
            r = self.stack.pop()
            l = self.stack.pop()
            self.root = op
            self.root.left = l
            self.root.right = r
            self.stack.append(self.root)
            return self.root
        else:
            self.stack.append(new_node)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def prefix(self, node):
        if node != None:
            print(str(node), end="")
            self.prefix(node.left)
            self.prefix(node.right)

    def infix(self, node):
        global preset
        if node != None:
            if node.right is not None or node.left is not None:
                preset += "("
            self.infix(node.left)
            preset += str(node)
            self.infix(node.right)
            if node.right is not None or node.left is not None:
                preset += ")"


T = BST()
inp = input("Enter Postfix : ")
for s in inp:
    root = T.insert(s)
print("Tree :")
T.printTree(root)
print("--------------------------------------------------")
T.infix(root)
print(preset)
print("Prefix : ", end="")
T.prefix(root)

