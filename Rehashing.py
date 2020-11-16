import math
class Hash:
    def __init__(self,max_size,max_col,threshold):
        self.max_size = max_size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * max_size
        self.current_size = 0
    def __str__(self):
        ss = ""
        for i in range(1,self.max_size+1):
            ss += f"#{i}	{self.table[i-1]}\n"
        return ss[:-1]

    def expand(self,x):
        prime = findPrime(self.max_size * 2)
        addition_table = [None] * (prime - self.max_size)
        self.table.extend(addition_table)
        self.max_size = len(self.table)
        self.add(x)

    def add(self, x):
        print(self.current_size)
        t = self.table
        indx = x % self.max_size
        if t[indx] == None:
            t[indx] = x
            self.current_size += 1
            return
        else:
            i = 0
            collision = 0
            while t[(indx + pow(i,2)) % self.max_size] != None:
                i += 1
                collision += 1
                print(f"collision number {collision} at {(indx + pow(i,2)) % self.max_size}")
                if collision >= self.max_col:
                    print("****** Max collision - Rehash !!! ******")
                    self.expand(x)
                    return
            t[(indx + pow(i,2)) % self.max_size] = x
            self.current_size += 1

        if (self.current_size / self.max_size) * 100 >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.expand(x)


def findPrime(num,i=2):
    if num > 1:
        if num % i == 0:
            return findPrime(num+1,i+1)
        else:
            return num
    
    
inp = input("Enter Input : ").split("/")
max_size, max_col, threshold = list(map(int,inp[0].split()))
items = list(map(int,inp[1].split()))
print("Initial Table :")
H = Hash(max_size,max_col,threshold)
for item in items:
    print("Add :",item)
    H.add(item)
    print(H)
    print("----------------------------------------")
    
    
        
