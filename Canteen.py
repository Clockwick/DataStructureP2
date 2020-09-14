class Queue:

    def __init__(self, lst=None):
        self.queue = lst if lst is not None else []

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        output = ""
        if not self.isEmpty():
            for i in self.queue:
                output += str(i) + ' '
        else:
            output = 'Empty'
        return output

    def put(self, i):
        self.queue.append(i)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Empty"

    def is_in_group(self, group):
        for i in self.queue:
            if group == i[0]:
                return True
        return False

    def putFront(self, val):
        if self.isEmpty() or not self.is_in_group(val[0]):
            self.put(val)
        else:
            for i in range(self.size()-1, -1, -1):
                if self.queue[i][0] == val[0]:
                    self.queue.insert(i+1, val)
                    return
            self.put(val)

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
    n, q = input("Enter Input : ").split("/"), Queue()
    e = n[0].split(",")
    emp = dict()
    for r in e:
        g, Id = r.split()
        emp[Id] = g
    action = n[1].split(",")
    for i in action:
        if len(i) == 1:
            if not q.isEmpty():
                print(q.get()[1])
            else:
                print("Empty")
        else:
            l = i.split()
            val = l[1]
            q.putFront((emp[val], val))

