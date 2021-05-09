""" 
Mergesort Implementation

"""


## @brief The merge part of the sorting
#  @details merge the array according to each subarray
#  @param arr the list that contains the value
#  @param l the low index of the array
#  @param m the middle index
#  @param r the last index
def merge(arr, l, m, r,order):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if cmp(L,R,i,j,order):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def cmp(L,R,i,j,order='ascend'):
    if order == 'ascend':
       return L[i] <= R[j]
    else:
        return L[i] > R[j]


## @brief The recursive merging part
#  @details we sort the array in a top-down fashion by divide and conquer
#  @param arr the list that contains the value
#  @param l the low index of the array
#  @param r the last index

def mergeSort(arr, l, r,order='ascend'):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m,order)
        mergeSort(arr, m + 1, r,order)
        merge(arr, l, m, r,order)



