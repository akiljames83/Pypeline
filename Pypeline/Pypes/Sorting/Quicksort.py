

## @brief The partition part of the sorting
#  @details the index for the partition element is returned
#  @param arr the list that contains the value
#  @param low the low index of the array
#  @param high the last index
#  @return an index of the partition element is returned
def partition(arr, low, high,order):
    i = (low -1)
    pivot = arr[high]

    for j in range(low, high):
        if cmp(arr[j],pivot,order):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def cmp(a,b,order='ascend'):
    if order == 'ascend':
        return a <= b
    else:
        return a > b


## @brief The recursive part of the sorting
#  @details we recursively quicksort the left and right part of the partitioning element
#  @param arr the list that contains the value
#  @param low the low index of the array
#  @param high the last index
def quickSort(arr, low, high,order='ascend'):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high,order)
        quickSort(arr, low, pi - 1,order)
        quickSort(arr, pi + 1, high,order)





