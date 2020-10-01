class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def __str__(self):
    s=""
    current = self.head
    while current:
      s+=str(current.data) + ", "
      current = current.next
    return s[:-2]
  def append(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
  def remove(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current == self.tail:
          self.tail = self.tail.prev
          self.tail.next = None
        elif current == self.head:
          self.head = self.head.next
          self.head.prev = None
        else:
          current.prev.next = current.next
          current.next.prev = current.prev
      
      current = current.next
  def pop(self, i = None):
    if i == None:
      if self.size() > 1:
        self.tail = self.tail.prev
        self.tail.next = None
      else:
        self.head = None
        self.tail = None
    else:
      current = self.head
      for _ in range(i-1):
        current = current.next
      self.remove(current.data)

  def addHead(self, data):
    if self.isEmpty():
      self.append(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
      
  def insert(self, data, i):
      new_node = Node(data)
      for _ in range(i):
        current = current.next
      new_node.prev = current.prev
      new_node.next = current
      current.prev = new_node
      
  def size(self):
    current = self.head
    si = 0
    while current:
      si += 1
      current = current.next
    return si
  def isEmpty(self):
    return self.size() == 0
  def index(self, i):
    if i < 0:
      i += self.size()
    if 0 <= i < self.size():
      current = self.head
      for _ in range(i):
        current = current.next
      return current.data
    else:
      return "Out of Range"
    

  def search(self, data):
    s = 0
    current = self.head
    while current:
      if current.data == data:
        return self.index(s)
      current = current.next
      s += 1
        
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None


ll = DoublyLinkedList()
ll.append(10)
ll.append(15)
ll.append(20)
print(ll)
ll.remove(20)
ll.remove(10)
ll.append(10)
ll.append(15)
ll.append(20)
print(ll)
ll.pop()
ll.pop()
ll.pop()
ll.pop()
ll.pop()
print(ll)
ll.append(10)
ll.append(20)
print(ll)
ll.addHead(5)
ll.addHead(8)
print(ll)
print(ll.index(4))
print(ll.index(-1))
print(ll.index(4))
print(ll.index(-4))