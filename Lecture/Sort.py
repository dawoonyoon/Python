def selection_sort(L):
	for i in range(len(L)-1):
		min_index = i
		for j in range(i+1, len(L)-1):
			if L[j] < L[min_index]:
				min_index = j
		L[i], L[min_index] = L[min_index], L[i]
L = [3, 1, 41, 59, 26, 53, 59]
print(L)
selection_sort(L)
print(L)

def selection_sort(arr):
	for i in range(len(arr)-1):
		min_idx=1
		#최소값 찾는 처리
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		#최소값의 위치를 바꿔주는 처리
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [4, 0, 42, 60, 15, 88, 187]
print(arr)
selection_sort(arr)
print(arr)

'''
def bubble_sort(our_list):
	for i in range(len(our_list)):
		for j in range(len(our_list) - 1):
			if our_list[j] > our_list[j+1]:
				our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
our_list=[19,13,6,2,18,8]
print(our_list)
bubble_sort(our_list)
print(our_list)
'''

'''
def selection_sort(arr):
	for i in range(len(arr)-1):
		min_idx=1
		#최소값 찾는 처리
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		#최소값의 위치를 바꿔주는 처리
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
'''