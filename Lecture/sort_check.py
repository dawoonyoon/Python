def selection_sort(arr):
	for i in range(len(arr)-1):
		min_idx=1
		#최소값 찾는 처리
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		#최소값의 위치를 바꿔주는 처리
		arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
	for i in range(len(arr) - 1, 0, -1):
		for j in range(i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

'''def insertion_sort(arr):
	for end in range(1, len(arr)):
		for i in range(end, 0, -1):
			if arr[i - 1] > arr[i]:
				arr[i - 1], arr[i], arr[i - 1]'''

def insertion_sort(arr):
	for end in range(1, len(arr)):
		to_insert = arr[end]
		i = end
		while i > 0 and arr[i - 1] > to_insert:
			arr[i] = arr[i - 1]
			i -= 1
		arr[i] = to_insert

a = [2, 1, 5, 4, 3]

print(selection_sort(a))