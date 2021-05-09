
## @brief Shellsort algorithm
#  @details Modified version of insertion sort
#  @param arr the list that contains the value
def shellSort(arr,order="ascend"):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while condition(j,gap,arr,temp,order):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

def condition(j,gap,arr,temp,order = 'ascend'):
    if order == 'ascend':
        return j >= gap and arr[j - gap] > temp
    else:
        return  j >= gap and arr[j - gap] < temp




