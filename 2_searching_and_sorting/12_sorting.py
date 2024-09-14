import numbers
def calc_min(arr):
    #counter = 0
    min = arr[0]
    for i in arr:
        if isinstance(i, numbers.Number) and not (isinstance(i, bool)):
            if i < min:
                min = i
    #print(min)
    return min

array = [1,2,3,4,1,1,-10,10,-10,100, -3.6]
#print(array[:-1])
calc_min(array)

# Selection sort:
def selection_sort(my_arr=[]):
    arr = my_arr.copy()
    sorted_arr = []
    while len(arr)>0:
        min = calc_min(arr)
        arr.remove(min)
        sorted_arr.append(min)
    
    return(sorted_arr)

#print(selection_sort(array))

def bubble_sort(my_arr=[]):
    arr = my_arr.copy()
    sorted_arr = []
    while arr != sorted_arr:
        sorted_arr = arr.copy()
        for i in range(len(arr)-1):
            first = arr[i]
            second = arr[i+1]
            if first > second:
                arr[i] = second
                arr[i+1] = first          
    return(sorted_arr)
        

#print(array)
#print(bubble_sort(array))

#Insertion Sort
def insertion_sort(my_arr=[]):
    arr = my_arr.copy()
    sorted_arr = []
    while arr != sorted_arr:
        sorted_arr = arr.copy()
        for i in range(len(arr)-1):
            first = arr[i]
            second = arr[i+1]
            if first > second:
                arr[i] = second
                arr[i+1] = first
                for j in range(i-1):
                    first_j = arr[i-1-j]
                    second_j = arr[i-j]
                    if first_j > second_j:
                        arr[i-1-j] = second_j
                        arr[i-j] = first_j

    return(sorted_arr)

#print(array)
#print(insertion_sort(array))

# Counting sort -- Solo funciona con integers
def counting_sort(my_arr=[]):
    arr = my_arr.copy()
    min = calc_min(arr)
    arr = [x-min for x in arr]
    max = -1*calc_min([-x for x in arr])
    counts = [0]*(max+1)
    sorted_arr = []
    for element in arr:
        counts[element] +=1
    for i in range(len(counts)):
        if counts[i] > 0:
            sorted_arr.extend([i]*counts[i])
    sorted_arr = [x+min for x in sorted_arr]
    return(sorted_arr)

array =[10,9,-2,2,2,1,2,23,0,-4,5]
print(array)
print(counting_sort(array))


