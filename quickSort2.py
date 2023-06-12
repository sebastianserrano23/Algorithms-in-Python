# another implementation of quick sort
def partition(A, l, r):
    pivot = A[r]
    i = l
    j = r
    while i < j:
        while A[i] <= pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        A[i], A[j] = A[j], A[i]
    A[i], A[r] = A[r], A[i]
    return i



    