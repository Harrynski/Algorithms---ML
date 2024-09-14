
a1= [1,1,2,7]
a2= [1,2,2,4,18]

def merge(array1,array2):
    arr1, arr2 = array1.copy(), array2.copy()
    merged_arr = []
    while (arr1 or arr2):
        if (arr1 and arr2):
            min_element = min(arr1[0], arr2[0])
            merged_arr.append(min_element)
            if min_element==arr1[0]: arr1.pop(0)
            elif min_element == arr2[0]: arr2.pop(0)
        elif arr1:
            merged_arr.extend(arr1)
            return(merged_arr)
        elif arr2:
            merged_arr.extend(arr2)
            return(merged_arr)   
    return(merged_arr)

def merge_sort(arr):
    if len(arr)<2:
        return(arr)
    else:
        medium_point = (len(arr))//2
        arr1 = arr[:medium_point]
        arr2 = arr[medium_point:]
        print(arr1,arr2)
        sorted_1 = merge_sort(arr1)
        sorted_2 = merge_sort(arr2)
        print(sorted_1,sorted_2)
        
        return(merge(sorted_1,sorted_2))

#print(merge_sort([1,3,2,1,686,12,3,-10]))


# Quick Sort

import random


def quick_sort(arr):
    if len(arr)<2:
        return(arr)
    else:
        random_index = random.randint(0, len(arr)-1)
        pivot = arr[random_index]

        arr1 = [x for x in arr if x<pivot]
        arr2 = [x for x in arr if x>pivot]
        arr3 = [x for x in arr if x==pivot]

        sorted_1 = quick_sort(arr1)
        sorted_2 = quick_sort(arr2)

        return(merge(merge(sorted_1,arr3),sorted_2))
    