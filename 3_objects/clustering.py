import numpy as np

def assign_random_group(data_list, K=3):
    datalist = data_list.copy()
    group_number = 0 
    for vector in datalist:
        group_number = (group_number % K)
        vector.insert(0,group_number)
        group_number +=1
    return datalist

def mean(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return 0
    # Sum all the numbers and divide by the length of the list
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def calculate_centroids(data_list, K=3, D=4):
    centroids = []
    for n in range(K):
        #print(n)
        centroid = []
        for d in range(1,D+1):
            #print(d)
            dimension_values = []
            for vector in data_list:
                if vector[0]== n:
                    dimension_values.append(vector[d])
            #print(dimension_values)
            centroid.append(mean(dimension_values))
        centroids.append(centroid)
    return centroids

def absolute_diff(x,y):
    if (x-y >= 0):
        return(x-y)
    else:
        return(y-x)

def euclidean_distance(vector1, vector2):
    # suponiendo que tienen igual dimensiones
    sum = 0
    for i in range(len(vector1)):
        diff = (vector1[i]-vector2[i])**2
        sum += diff
    return np.sqrt(sum)
          
def find_closest_centroid(data_list, centroid_list):
    datalist = data_list.copy()
    for vector in datalist:
        #current_group = vector[0]
        minimum_distance = None
        reassigned_group = None
        for centroid_index, centroid in enumerate(centroid_list):
            distance = euclidean_distance(vector[1:], centroid)

            if (minimum_distance is None) or (distance < minimum_distance):
                minimum_distance = distance
                reassigned_group = centroid_index

        vector[0] = reassigned_group
    return datalist
        
data = [
[0.14 , 0.14 , 0.28 , 0.44] ,
[0.22 , 0.1 , 0.45 , 0.33] ,
[0.1 , 0.19 , 0.25 , 0.4 ] ,
[0.02 , 0.08 , 0.43 , 0.45] ,
[0.16 , 0.08 , 0.35 , 0.3 ],
[0.14 , 0.17 , 0.31 , 0.38] ,
[0.05 , 0.14 , 0.35 , 0.5 ],
[0.1 , 0.21 , 0.28 , 0.44] ,
[0.04 , 0.08 , 0.35 , 0.47] ,
[0.11 , 0.13 , 0.28 , 0.45] ,
[0.0 , 0.07 , 0.34 , 0.65] ,
[0.2 , 0.05 , 0.4 , 0.37] ,
[0.12 , 0.15 , 0.33 , 0.45] ,
[0.25 , 0.1 , 0.3 , 0.35] ,
[0.0 , 0.1 , 0.4 , 0.5 ],
[0.15 , 0.2 , 0.3 , 0.37] ,
[0.0 , 0.13 , 0.4 , 0.49] ,
[0.22 , 0.07 , 0.4 , 0.38] ,
[0.2 , 0.18 , 0.3 , 0.4 ] 
]
#print(data[0])
#data = assign_random_group(data, K=5)
#print(data[0])
#print("")
#centroids = calculate_centroids(data)
#print(centroids)
#print("")
#data = find_closest_centroid(data, centroids)
#print(data)
#print("")
#centroids = calculate_centroids(data)
#print(centroids)
#print("")
#data = find_closest_centroid(data, centroids)
#print(data)
#print("")

def k_means_clustering(data_list, **kwargs ):
    datalist = data_list
    datalist = assign_random_group(data_list, **kwargs )
    new_centroid_data = []
    while data != new_centroid_data:
        new_centroid_data = datalist
        centroids = calculate_centroids(datalist, K=5)
        datalist = find_closest_centroid(datalist, centroids)
    print(centroids)
    return datalist


for list in k_means_clustering(data):
    print(list)
    print("")