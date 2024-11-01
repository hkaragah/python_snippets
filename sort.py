def bubbleSort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




def mergeSort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        # print(f"Splitting: left={left}, right={right}")
        mergeSort(left)
        mergeSort(right)
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
                
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        # print(f"Merging: {arr}")
    return arr
 

     



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + mid + quicksort(right)



def main():
    arr =  [54,26,93,17,77,31,44,55,20]
    print(f"Unsorted array: {arr}\n")
    print(f"Sorted array: {mergeSort(arr)}")
       
    arr = [54,26,93,17,77,31,44,55,20]
    print(quicksort(arr)) 
        
        
        
import os
import unittest

class TestSort(unittest.TestCase):
    def setUp(self):
        self.arr = [54,26,93,17,77,31,44,55,20]
        self.sorted_arr = [17, 20, 26, 31, 44, 54, 55, 77, 93]    
        
    def tearDown(self):
        pass
    
    def testBubbleSort(self):
        self.assertEqual(bubbleSort(self.arr), self.sorted_arr)
        
    def testMergeSort(self):
        self.assertEqual(mergeSort(self.arr), self.sorted_arr)
        
    def testQuickSort(self):
        self.assertEqual(quicksort(self.arr), self.sorted_arr)
        
        
if __name__ == "__main__":
    os.system('cls') if os.name == 'nt' else os.system('clear')
    unittest.main()
    # main()