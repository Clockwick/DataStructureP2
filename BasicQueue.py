class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def put(self, i):
        self.queue.append(i)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return -1


if __name__ == "__main__":
    n, q, num = input("Enter Input : ").split(","), Queue(), 0
    for i in n:
        if i[0] == "E":
            value = int(i.partition(" ")[2])
            q.put(value)
            print(f"Add {value} index is {num}")
            num += 1
        else:
            if len(q) > 0:
                num -= 1
                print(f"Pop {q.get()} size in queue is {len(q)}")
            else:
                print(q.get())

    if len(q) > 0:
        print(f"Number in Queue is :  {list(map(str,q.queue))}")
    else:
        print("Empty")
