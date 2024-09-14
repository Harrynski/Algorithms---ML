import math
import numpy as np
#3
def f(x,y):
    return(x*math.sin(y)+x**2)

def f_x(x,y):
    return(math.sin(y)+2*x)

def f_y(x,y):
    return(x*math.cos(y))

def gradient_f(vector):
    x=vector[0]
    y=vector[1]
    return(np.array([f_x(x,y), f_y(x,y)]))

def mv_gradient_descent(alfa=0.01, starting_point=[1,2], iterations=3001):
    x = np.array(starting_point)
    for step in range(iterations):
        x = x - alfa * gradient_f(x)
        #  if step %100==0:
            #print(step, x, gradient_f(x))
    return(x)

def random_generator(inf=-10,sup=10, dimension=2):
    random_vector = []
    for dim in range(dimension):
        random_int = random.randint(inf, sup)
        random_vector.append(random_int)
    return(np.array(random_vector))

def multi_start_g_d(trials=100, **kwargs):
    minima_list = []
    for trial in range(trials):
        
        starting_x = random_generator(**kwargs)
        print('empezamos con: ', starting_x)
        try:
            minima = mv_gradient_descent(starting_point = starting_x, **kwargs)
            minima_list.append(minima)
        except:
            pass
    return(min(minima_list))


print(mv_gradient_descent())
'''
print(np.array([1,1]) - np.array([1,1]))
[1,1]-[2,2]

import numpy as np
a = np.array([1,1]) 
print(2*a)'''