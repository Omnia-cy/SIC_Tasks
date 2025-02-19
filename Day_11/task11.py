
def lenn(list, len=0):
    if not list:
        return len
    return 1 + lenn(list[1:], len)
list = [1,2,3]
print(lenn(list))


def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = []
        greater = []
        for x in list[1:]:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return quick_sort(less) + [pivot] + quick_sort(greater)

list = [10, 7, 8, 9, 1, 5,1,1]
sorted_arr = quick_sort(list)
print("Sorted array:", sorted_arr)
# what is the defferance between (mid,left-1,-1) and (left,mid+1)


##################################################################


# (mid,left-1,-1)

def quick_sort_left(arr, low, high):
    if low < high:
        pivot = partition_left(arr, low, high)
        quick_sort_left(arr, low, pivot - 1)
        quick_sort_left(arr, pivot + 1, high)


def partition_left(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Example usage
nums = [4, 2, 7, 1, 3, 6, 5]
quick_sort_left(nums, 0, len(nums) - 1)
print(nums)


#################################################################################3


#(left,mid+1)

def quick_sort_right(arr, low, high):
    if low < high:
        pivot = partition_right(arr, low, high)
        quick_sort_right(arr, low, pivot - 1)
        quick_sort_right(arr, pivot + 1, high)


def partition_right(arr, low, high):
    pivot = arr[low]
    left = low
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Example usage
nums = [4, 2, 7, 1, 3, 6, 5]
quick_sort_right(nums, 0, len(nums) - 1)
print(nums)





