#Solution_1(by Sorting)
#_______________________
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


Find_Largest_K_Sort = lambda list, k: list[-k]
################################################################
#Solution_2(Without Sort)
#_____________________
def Find_Largest_K_Stack(list, k):
    listt = []
    for num in list:
        if len(listt) < k:
            listt.append(num)
        else:
            min_value = min(listt)
            if num > min_value:
                listt.remove(min_value)
                listt.append(num)

    return min(listt)

################################################################
#Solution_3(by Heap)
#_____________________
import heapq
def Find_Largest_K_Heap(list, k):
    heap = []

    for num in list:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

    return heap[0]


################################################################
list = input("Enter elements: ").split()
list = quick_sort(list)

k = int(input("Enter the value of k: "))
value_1 = Find_Largest_K_Sort(list, k)
value_2 = Find_Largest_K_Stack(list,k)
value_3 = Find_Largest_K_Heap(list,k)
print("Kth largest element in the list is : ", value_1,",",value_2,",",value_3)
