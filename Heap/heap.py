class MinHeap:
    size = 0
    heap = [10000000] * 1000
    
    def push(self,x):
        heap = self.heap
        heap[self.size] = x
        current = self.size
        while current > 0 and heap[current] < heap[(current-1)//2]:
            heap[current], heap[(current-1)//2] = heap[(current-1)//2], heap[current]
            current = (current-1)//2
        self.size += 1

    def pop(self):
        heap = self.heap
        size = self.size
        heap[0], heap[size - 1] = heap[size - 1], heap[0]
        current = 0
        temp = heap[size - 1]
        heap[size - 1] = 10000000
        while heap[current] > heap[2*current+1] or heap[current] > heap[2*current + 2]:
            if heap[2*current + 1] < heap[2*current + 2]:
                heap[current], heap[2*current + 1] = heap[2*current + 1], heap[current]
                current = 2*current + 1
            else:
                heap[current], heap[2*current + 2] = heap[2*current + 2], heap[current]
                current = 2*current + 2
        self.size -= 1
        return temp

def heap_sort(arr):
    H = MinHeap()
    for item in arr:
        H.push(item)
    for i in range(len(arr)):
        arr[i] = H.pop()
    return arr
        
arr = [8, 12, 13, 16, 17, 19, 2, 12, 0, 11, 11, 9, 19, 19, 0, 14, 18, 20, 9, 3]
print("Unsorted array :", arr)
sort_arr = heap_sort(arr)
print("Sorted array :", sort_arr)