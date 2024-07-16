#CLRS logic

import math

def parent(i):
	return math.ceil(i/2) - 1

def left(i):
	return 2*i + 1 

def right(i):
	return 2*i + 2 

def max_heapify(A, i, heap_size):
	l = left(i)
	r = right(i)
	if l < heap_size and A[l] > A[i]:
		largest = l
	else:
		largest = i 
	if r < heap_size and A[r] > A[largest]:
		largest = r 

	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest, heap_size)

def build_max_heap(A):
	n = len(A)
	for i in range(n//2):
		max_heapify(A, n//2 - i - 1, n)

def heap_sort(A):
	build_max_heap(A)
	heap_size = len(A)
	n = heap_size
	for i in range(n-1):
		A[0], A[n - i - 1] = A[n - i - 1], A[0]
		max_heapify(A, 0, heap_size - 1)
		heap_size -= 1
	return A  

def pop_heap(A, heap_size):
	A[0], A[heap_size-1] = A[heap_size-1], A[0]
	max_heapify(A, 0, heap_size-1)
	return A[heap_size-1], heap_size-1


if __name__ == '__main__':
	import random
	A = [random.randint(0,100) for _ in range(100)]
	print(A)
	heap_sort(A)
	print(A)

	A = [random.randint(0,100) for _ in range(100)]
	print("for extracting max: \n", A)
	build_max_heap(A)
	max_, heap_size = pop_heap(A, len(A))
	print(max_, heap_size)
	max_, heap_size = pop_heap(A, heap_size)
	print(max_, heap_size)
