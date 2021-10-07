#Comparing sorting algorithms
import random as rd
import time

#Sorting ALgorithms
#Merge Sort
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

#Quick Sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

#Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

#Insertion Sort
def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

#Performance Tests
#Merge Sort
def merge_test(k = 100):
    m = [rd.randint(1, 2*k) for i in range(k)]
    t0 = time.perf_counter()
    sortedList = merge_sort(m)
    t = time.perf_counter()
    print('Merge sort', k, 'items costs', t-t0, 'seconds.')

#Quick Sort
def quick_test(k = 100):
    m = [rd.randint(1, 2*k) for i in range(k)]
    t0 = time.perf_counter()
    sortedList = quick_sort(m)
    t = time.perf_counter()
    print('Quick sort', k, 'items costs', t-t0, 'seconds.')

#Bubble Sort
def bubble_test(k = 100):
    m = [rd.randint(1, 2*k) for i in range(k)]
    t0 = time.perf_counter()
    sortedList = bubble_sort(m)
    t = time.perf_counter()
    print('Bubble sort', k, 'items costs', t-t0, 'seconds.')

#Insertion Sort
def insertion_test(k = 100):
    m = [rd.randint(1, 2*k) for i in range(k)]
    t0 = time.perf_counter()
    sortedList = insertion_sort(m)
    t = time.perf_counter()
    print('Insertion sort', k, 'items costs', t-t0, 'seconds.')

#Main Function
if __name__ == '__main__':
    merge_test()
    quick_test()
    bubble_test()
    insertion_test()