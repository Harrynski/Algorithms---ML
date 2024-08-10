#Starting with 5, generate each term by multiplying the previous term by 3 and subtracting 4.
#Starting with 25, generate each term by taking half of the previous term if it's even, or multiplying by 
#3 and adding 1 if it's odd. (This is an instance of a Collatz sequence.)
#Starting with 0,1, generate each term by adding the previous two terms. (This is the famous Fibonacci sequence.)
#Starting with 2,−3, generate each term by adding the product of the previous two terms.

# 1
def calc_times_3_minus_4(terms):
    if terms==1:
        return(5)
    else:
        previous_term = calc_times_3_minus_4(terms-1)
        return(previous_term*3-4)
# 2
def calc_collatz(terms):
    if terms==1:
        return(25)
    else:
        previous_term = calc_collatz(terms-1)
        if previous_term%2==0:
            return(previous_term/2)
        else:
            return(previous_term*3+1)

#3
def calc_fibo(terms):
    if terms in [0,1]:
        return(1)
    else:
        previous_term = calc_fibo(terms-1)
        previous_previous_term = calc_fibo(terms-2)
        return(previous_term+previous_previous_term)
#4
def calc_recursion_4(terms):
    if terms == 1:
        return(2)
    if terms == 2:
        return(-6)
    else:
        previous_term = calc_recursion_4(terms-1)
        previous_previous_term = calc_recursion_4(terms-2)
        return(previous_term + previous_term*previous_previous_term)

for n in range(1,11):
    print(calc_recursion_4(n))