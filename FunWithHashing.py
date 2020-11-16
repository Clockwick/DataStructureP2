class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, max_col):
        self.current_size = 0
        self.size = size
        self.max_col = max_col
        self.table = [None] * size
    def __str__(self):
        ss = ""
        for i in range(1,self.size+1):
            ss += (f"#{i}	{self.table[i-1]}\n")
        return ss[:-1]
    def add(self, x): 
        first_word = x.split()[0]
        second_word = x.split()[1]
        size = self.size
        t = self.table
        asc = 0
        for d in first_word:
            asc += ord(d)
        indx = asc % size
        if t[indx] == None and self.current_size < size:
            t[indx] = Data(first_word, second_word)
            self.current_size += 1
        else:
            if self.current_size >= size:
                return 
            else:
                i = 0
                n = 1
                while (indx + pow(i,2)) % size < size:
                    hx = (indx + pow(i,2)) % size
                    if t[hx] == None:
                        t[hx] = Data(first_word, second_word)
                        self.current_size += 1
                        return
                    if n >= self.max_col:
                        print(f"collision number {n} at {hx}")
                        print("Max of collisionChain")
                        return
                    else:
                        print(f"collision number {n} at {hx}")
                    i += 1
                    n += 1
    def get_size(self):
        return self.current_size         
                             
print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split("/")
table_size, max_col = list(map(int,inp[0].split()))
data = inp[1].split(",")
hash_table = Hash(table_size, max_col)
for item in data:   
    hash_table.add(item)
    print(hash_table)
    print("---------------------------")
    if hash_table.get_size() >= table_size:
        print("This table is full !!!!!!")
        break






