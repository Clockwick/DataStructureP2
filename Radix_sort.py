class Node:
  def __init__(self ,data):
    self.data = data
    self.next = None
  
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 1
    self.zero = []
    self.check = 0
    self.isFirstRound = True
  def __str__(self):
    show_str = ""
    current = self.head
    while current:
      show_str += current.data + " -> "
      current = current.next
    show_str = show_str[:-4]
    return show_str
  def append(self, item):
    new_node = Node(item)
    current = self.head
    if current is None:
      self.head = new_node
      self.tail = new_node
      return
    while current.next:
      current = current.next
      self.tail = current
    current.next = new_node
    self.tail = new_node
    new_node.next = None
  def radix_sort(self): 
    print("------------------------------------------------------------")
    print(f"Round : {self.count}")
    self.check = 0
    self.cal_10digit()
    self.count += 1
    if self.check <= 9 and not self.zero:
      self.radix_sort()
    else:
      print("------------------------------------------------------------")
      print(f"{self.count - 2} Time(s)")
      print("Before Radix Sort :", self)
      print("After Radix Sort :", " -> ".join(self.zero))

  def cal_10digit(self):
    for i in range(10):
      if i == 0 and self.isFirstRound:
        temp = self.real_math(i)
        print(f"{i} : {temp}")
        self.isFirstRound = False
      elif i == 0 and not self.isFirstRound:
        self.real_math(i)
        show_zero = " ".join(self.zero)
        print(f"{i} : {show_zero}")
      else:
        print(f"{i} : {self.real_math(i)}")
  def real_math(self, digit): # return ทุกตัวที่ลงท้ายด้วย i
    current = self.head
    temp_str = ""
    temp_list = []
    temp_compare = []
    while current:
      if self.get_digit(current.data) == digit:
        temp_compare.append(current.data)
      elif self.get_digit(current.data) == -1:
        temp_list.append(current.data)
      current = current.next
    if temp_compare == []:
      self.check += 1
    temp_compare = list(map(int, temp_compare))
    temp_compare.sort()
    temp_compare = list(map(str, temp_compare))
    temp_str = " ".join(temp_compare)
    temp_list = list(map(int, temp_list))
    temp_list.sort()
    temp_list = list(map(str, temp_list))
    self.zero = temp_list
    return temp_str

  def get_digit(self, n):
    if int(n) < 0:
      n = str(abs(int(n)))
    else:
      n = str(n)
    count = self.count
    if len(n) < count:
      return -1
    return int(n[len(n)-count])
    

if __name__ == "__main__":
  n = input("Enter Input : ").split()
  ll = LinkedList()
  for i in n:
    ll.append(i)
  ll.radix_sort()
  