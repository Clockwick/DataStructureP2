def binary_search1(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
def binary_search2(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if x is present at mid 
        if arr[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif arr[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1
  
lst = [4, 3, 17, 16, 14, 13, 6, 0, 18, 1, 2, 20, 5, 19, 15, 8, 9, 7, 12, 11, 10]
x = 16
print ("==LinearSearch==")
print(lst.index(x))
print ("==BinarySearchWithRecursive==")
print(binary_search1(lst,0,len(lst)-1,x))
print ("==BinarySearchWithIterative==")
print(binary_search1(lst,0,len(lst)-1,x))



  



        




