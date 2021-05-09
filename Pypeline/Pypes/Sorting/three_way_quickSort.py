def cmp(a, b, order='ascend'):
    if order == 'ascend':
        if a == b:
            return 0
        elif (a > b):
            return 1
        else:
            return -1
    else:
        if a == b:
            return 0
        elif (a > b):
            return -1
        else:
            return 1


def exch(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


## @brief 3-way quick sort with 3-way partition
#  @details This sorting method largely improved running time of sequence with large duplicate keys
#  @param arr the list that contains the value
#  @param lo the low index of the array
#  @param hi the last index
#  @param order specify the order of the sorting

def three_way_quickSort(arr, lo, hi, order='ascend'):
    if hi <= lo:
        return
    lt = lo
    i = lo + 1
    gt = hi
    v = arr[lo]
    while i <= gt:
        index = cmp(arr[i], v, order)
        if index < 0:
            exch(arr, lt, i)
            lt += 1
            i += 1
        elif (index > 0):
            exch(arr, i, gt)
            gt -= 1
        else:
            i += 1
    three_way_quickSort(arr, lo, lt - 1, order)
    three_way_quickSort(arr, gt + 1, hi, order)