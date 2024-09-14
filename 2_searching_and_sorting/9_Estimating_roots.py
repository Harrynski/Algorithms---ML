#1. Write a script that approximates cubic root of 2 to a precision of 6 decimal places using bisection search. 
# (This should match up against the provided example and continue for more iterations.)

#buscamos x tal que x^3 = 2, luego x es la raíz cubica de 2. Es decir, buscamos una raíz de la función
# f(x) = x^3-2
# Sabemos que f(1)= -1 < 0 y f(2)>2>0, luego tomamos [1,2] como intervalo base.
def f(x):
    return(x**3-2)
#interval = [1,2]
def root_finder(precision, interval):
    current_precision = (interval[1]-interval[0])/2
    while current_precision>precision:
        mid_point = (interval[0]+interval[1])/2
        f_on_mid_point = f(mid_point)
        if f_on_mid_point > 0:
            interval = [interval[0], mid_point]
        else:
            interval = [mid_point, interval[1]]
        current_precision = (interval[1]-interval[0])/2
        print(mid_point)
    return(mid_point)

root_finder(precision = 0.00001, interval = [1,2])

#Writeafunction calc_root_bisection(a, n, precision) that approximates n√a raiz enesima de a 
# to the desired level of precision using bisection search.
def f(a, n, x):
    return(x**n-a)

def root_finder(a, n, precision):
    if not isinstance(n, int):
        raise ValueError('n should be an int')
    if n<0:
        raise ValueError('n should be positive')
    if a<0:
        raise ValueError('a should be positive')
    if precision<=0:
        raise ValueError('precision should be bigger than zero')
    interval = [0, a]
    mid_point = a/2 #f(a,n,)
    current_precision = a/4
    while current_precision>precision:
        f_on_mid_point = f(a=a, n=n, x = mid_point)
        if f_on_mid_point > 0:
            interval = [interval[0], mid_point]
        else:
            interval = [mid_point, interval[1]]
        mid_point = (interval[0]+interval[1])/2
        current_precision = (interval[1]-interval[0])/2
        print(mid_point)
    return(mid_point)

root_finder(precision = 0.00001, a=2, n=1000)




