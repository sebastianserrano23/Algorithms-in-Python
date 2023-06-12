# quick sort algorithm

def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while i < j:             # p  
        while A[i] <= pivot: # 6, 2, 3, 0, 4, 1, 9, 8 = A
            i += 1           # i           i  j       
        while A[j] > pivot: 
            j -= 1
    if i < j:
        A[i], A[j] = A[j], A[i]
    pivot, A[j] = A[j], pivot
    return j


def QuickSort(A, l, h):
    if l >= h:
        return
    j = partition(A, l, h)
    QuickSort(A, l, j)
    QuickSort(A, j + 1, h)
A = [9, 5,10, 3, 1, 2, 8, 4, 6, 7]

answer = QuickSort(A, 1, len(A) - 1)
print(answer)

