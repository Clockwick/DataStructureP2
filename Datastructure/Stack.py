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
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


s = Stack([1, 2, 3])
s.push(4)
print(s.pop())
print(s)
s.push(4)
s.push(5)
print(s.peek())
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
