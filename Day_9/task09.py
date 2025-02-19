
import random

BH = int(input("Enter the build height:"))
BF = random.randint(0, BH)

def linear_search(BF, BH):
    count = 0
    for f in range(0, BH):
        count += 1
        if f >= BF:
            return f, count
        
##########################################################################

def binary_search(BF, BH):
    left = 0
    right = BH
    count = 0
    while left <= right:
        count += 1
        mid = left + (right - left) // 2
        if mid == BF:
            return mid, count
        elif mid < BF:
            left = mid + 1
        else:
            right = mid - 1

    return left, count
##########################################################################

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


####################################################
def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

    
        arr[i], arr[min_index] = arr[min_index], arr[i]

   
##################################################


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
        
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        
        if not swapped:
            break
