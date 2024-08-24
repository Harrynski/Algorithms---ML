#Use gradient descent to minimize the following functions. 
# Before looking at the graph, perform gradient descent using several different initial guesses, 
# and then plug your final guesses back into the function to determine which final guess is the best 
# (i.e. gives you the lowest function value). Then, look at the graph to check whether you found
# the global maximum.
import random
import math

# 1. f(x)=x^2 +x+1 
#--- f'(x) = 2x +1
def f(x):
    return(x**2+x+1)
def d_f(x):
    return(2*x+1)
#2
def f(x):
    return(x**3-x**4-x**2)
def d_f(x):
    return(3*x**2-4*x**3-2*x)
#3
def f(x):
    return((math.sin(x))/(1+x**2))
def d_f(x):
    return((math.cos(x)+(x**2)*math.cos(x)-2*x*math.sin(x))/(1+2*x**2+x**4))


def gradient_descent(alfa=0.1, starting_point=1, iterations=100):
    x = starting_point
    for step in range(iterations):
        x = x - alfa* d_f(x)
        #print(x)
    return(x)

def random_generator(inf=-10,sup=10):
    random_int = random.randint(inf, sup)
    return(random_int)

def multi_start_g_d(trials=100, **kwargs):
    minima_list = []
    for trial in range(trials):
        
        starting_x = random_generator(**kwargs)
        print('empezamos con: ', starting_x)
        try:
            minima = gradient_descent(starting_point = starting_x, **kwargs)
            minima_list.append(minima)
        except:
            pass
    return(min(minima_list))



print(multi_start_g_d())
