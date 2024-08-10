
def copy_array(array):
    array_copy = []
    for element in array:
        array_copy.append(element)
    return(array_copy)

# dos

def cartesian_product_2(array_1, array_2):
    cartesian_product = []
    points = []
    #points = copy_array(cartesian_product)
    for item in array_1:
        point = copy_array(points)
        point.append(item)
        #print(point)
        for item2 in array_2:
            point_2 = copy_array(point)
            point_2.append(item2)
            cartesian_product.append(point_2)
    print(cartesian_product)


# tres

def cartesian_product_3(array_1, array_2, array_3):
    cartesian_product = []
    points = []
    #points = copy_array(cartesian_product)
    for item in array_1:
        point = copy_array(points)
        point.append(item)
        #print(point)
        for item2 in array_2:
            point_2 = copy_array(point)
            point_2.append(item2)
            #cartesian_product.append(point_2)
            for item3 in array_3:
                point_3 = copy_array(point_2)
                point_3.append(item3)
                cartesian_product.append(point_3)

    print(cartesian_product)



# general
def cartesian_product_gral(*lists):
    if len(lists) == 1:
        return [(item,) for item in lists[0]]
    cartesian_prod = []
    first_set = lists[0]
    remaining_prod = cartesian_product_gral(*lists[1:])

    for item in first_set:
        for product in remaining_prod:
            cartesian_prod.append((item,) + product)
    return cartesian_prod


arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']
arr3 = ['alfa', 'beta']

print(cartesian_product_gral(arr1,arr2, arr3))

'''
for point in points:
    point
    for item in array_1:
        #point = []
        point.append(item)
        #points.append(point)
        print(point)
cartesian_product.append(points)
print(cartesian_product)'''