class Queue:
    def __init__(self):
        self.queue = []
        self.psd = 0

    def __len__(self):
        return len(self.queue)

    def put(self, i):
        self.queue.append(i)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)[1]
        return "Empty"

    def putFront(self, val):
        if self.isEmpty():
            self.queue.append(val)
        elif self.peek()[0] == 'EN':
            self.queue.insert(0, val)
        else:
            for i in range(self.size()):
                if self.queue[i][0] == 'EN':
                    self.queue.insert(i, val)
                    return
            self.queue.append(val)

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.size() <= 0


if __name__ == "__main__":
    n, q = input("Enter Input : ").split(","), Queue()
    for i in n:
        ope = i.split()
        if len(ope) == 1:
            print(q.get())
        else:
            if ope[0] == 'EN':
                q.put((ope[0], ope[1]))
            elif ope[0] == 'ES':
                q.putFront((ope[0], ope[1]))
