class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def __str__(self):
        pass

    def enQ(self, i):
        self.items.append(i)

    def deQ(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "You cannot dequeue anymore because of queue is empty"

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
