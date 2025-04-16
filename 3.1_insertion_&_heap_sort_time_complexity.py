# -*- coding: utf-8 -*-
"""3-Insertion & Heap Sort Time Complexity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L1GOk1SqV2x_b0MPrVSaR4fRqnCdJZT8
"""

import time
import random
import matplotlib.pyplot as plt
import heapq

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Heap Sort
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


sizes = [200, 500, 1000, 7400, 20600]
times_insertion = []
times_heap = []

for n in sizes:
    arr = [random.randint(0, n) for _ in range(n)]

    arr_copy = arr[:]
    start_time = time.time()
    insertion_sort(arr_copy)
    end_time = time.time()
    times_insertion.append(end_time - start_time)

    arr_copy = arr[:]
    start_time = time.time()
    heap_sort(arr_copy)
    end_time = time.time()
    times_heap.append(end_time - start_time)

plt.plot(sizes, times_insertion, marker='o', linestyle='-', color='b', label="Insertion Sort")
plt.plot(sizes, times_heap, marker='s', linestyle='-', color='g', label="Heap Sort")
plt.xlabel('Number of elements (n)')
plt.ylabel('Time taken (seconds)')
plt.title('Insertion Sort vs Heap Sort Time Complexity')
plt.legend()
plt.grid()
plt.show()