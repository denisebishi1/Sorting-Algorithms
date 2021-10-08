# Comparing sorting algorithms
import random as rd
import time

# global variables
k = 10000  # elements to sort


# used for bubble merge and insert average case
def create_random_list(k, start=1, end=(k * 2)):
    arr = []
    tmp = rd.randint(start, end)
    for i in range(k):
        while tmp in arr:
            tmp = rd.randint(start, end)
        arr.append(tmp)
    return arr


# used for bubble merge and insert best case
def create_sorted_list(k, start=1, end=(k * 2)):
    arr = []
    tmp = rd.randint(start, end)
    for x in range(k):
        while tmp in arr:
            tmp = rd.randint(start, end)
        arr.append(tmp)
    arr.sort()
    return arr


# used for bubble merge and insert worst case
def create_reverse_list(k, start=1, end=(k * 2)):
    arr = []
    tmp = rd.randint(start, end)
    for x in range(k):
        while tmp in arr:
            tmp = rd.randint(start, end)
        arr.append(tmp)
    arr.sort(reverse=True)
    return arr


# SORTING ALGORITHMS

# Merge Sort
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
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


# Quick Sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


# Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr


# Insertion Sort
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


# PERFORMANCE TESTS

# Bubble Sort
def get_bubble_time(list):
    t0 = time.perf_counter()
    bubble_sort(list)
    t = time.perf_counter()
    t_passed = t - t0
    return t_passed


# Merge Sort
def get_merge_time(list):
    t0 = time.perf_counter()
    merge_sort(list)
    t = time.perf_counter()
    t_passed = t - t0
    return t_passed


# Insertion Sort
def get_insertion_time(list):
    t0 = time.perf_counter()
    insertion_sort(list)
    t = time.perf_counter()
    t_passed = t - t0
    return t_passed


# Quick Sort
def get_quick_time(list):
    t0 = time.perf_counter()
    quick_sort(list)
    t = time.perf_counter()
    t_passed = t - t0
    return t_passed


# Runs bubble sort 100 times and gets the average time
def get_avg_bubble(list):
    sum_num = 0.00
    for i in range(100):
        num = get_bubble_time(list)
        sum_num = sum_num + num
    avg = sum_num / 100
    return avg


# Runs merge sort 100 times and gets the average time
def get_avg_merge(list):
    sum_num = 0.00
    for i in range(100):
        num = get_merge_time(list)
        sum_num = sum_num + num
    avg = sum_num / 100
    return avg


# Runs insertion sort 100 times and gets the average time
def get_avg_insertion(list):
    sum_num = 0.00
    for i in range(100):
        num = get_insertion_time(list)
        sum_num = sum_num + num
    avg = sum_num / 100
    return avg


# Main Function
if __name__ == '__main__':
    # create random lists
    random_ls = create_random_list(k)
    sort_ls = create_sorted_list(k)
    reverse_ls = create_reverse_list(k)

    print("Bubble Sort best case: ", get_avg_bubble(sort_ls), " seconds to sort a list with ", k, " items.")
    print("Bubble Sort average case: ", get_avg_bubble(random_ls), " seconds to sort a list with ", k, " items.")
    print("Bubble Sort worst case: ", get_avg_bubble(reverse_ls), " seconds to sort a list with ", k, " items.")

    random_ls = create_random_list(k)
    sort_ls = create_sorted_list(k)
    reverse_ls = create_reverse_list(k)
    print("Merge Sort best case: ", get_avg_merge(sort_ls), " seconds to sort a list with ", k, " items.")
    print("Merge Sort average case: ", get_avg_merge(random_ls), " seconds to sort a list with ", k, " items.")
    print("Merge Sort worst case: ", get_avg_merge(reverse_ls), " seconds to sort a list with ", k, " items.")

    random_ls = create_random_list(k)
    sort_ls = create_sorted_list(k)
    reverse_ls = create_reverse_list(k)
    print("Insertion Sort best case: ", get_avg_insertion(sort_ls), " seconds to sort a list with ", k, " items.")
    print("Insertion Sort average case: ", get_avg_insertion(random_ls), " seconds to sort a list with ", k, " items.")
    print("Insertion Sort worst case: ", get_avg_insertion(reverse_ls), " seconds to sort a list with ", k, " items.")

    # quick_time(random_ls)
