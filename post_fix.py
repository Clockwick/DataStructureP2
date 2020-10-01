
class Stack:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def __str__(self):
        n = map(str, self.items)
        return ",".join(n)

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return "You cannot pop from empty list"

    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if self.size():
            return self.items[-1]

    def size(self):
        return len(self.items)


lst = []
s = Stack()
for c in input("Enter Input : "):
    if c not in '+-*/()':
        lst.append(c)
    else:
        if c in '+-':
            while s.peek() == '*' or s.peek() == '/':
                lst.append(s.pop())
            s.push(c)
        elif c == ')':
            while s.peek() != '(':
                lst.append(s.pop())
            s.pop()
        else:
            s.push(c)
while not s.isEmpty():
    lst.append(s.pop())
print("".join(lst))
