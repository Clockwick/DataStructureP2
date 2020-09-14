
class queue:
    queue = []

    def __init__(self, lst=None):
        self.queue = [e for e in lst if lst is not None and e is not " "]

    def __len__(self):
        return len(self.queue)

    def put(self, i):
        self.queue.append(i)

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return -1


def encodemsg(q1, q2):
    string = q1.queue
    number = list(map(int, q2.queue))
    encode_msg = []

    for i in range(len(string)):
        asc = ord(string[i])
        asc += number[0]
        if asc > 90 and asc < 97 or asc > 122:
            asc -= 26
        encode_msg.append(chr(asc))
        temp = number.pop(0)
        number.append(temp)

    print(f"Encode message is :  {encode_msg}")


def decodemsg(q1, q2):
    string = q1.queue
    number = list(map(int, q2.queue))
    decode_msg = [s for s in string if s is not " "]
    print(f"Decode message is :  {decode_msg}")


if __name__ == "__main__":
    string, number = input("Enter String and Code : ").split(",")
    q1 = Queue(string)
    q2 = Queue(number)
    encodemsg(q1, q2)
    decodemsg(q1, q2)
