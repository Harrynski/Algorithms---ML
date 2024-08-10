#check_if_symmetric(string)
#Return True if the input string is symmetric (i.e. a palindrome), and False if not. 
#You can ignore capitalization.
s1 = 'juan'
s2 = 'abba'
s3 = 'atysssyta'


def check_if_symmetric(string):
    string_copy = string
    inversed_string = ''
    for i in range(len(string_copy)):
        inversed_string = inversed_string + string_copy[-1]
        string_copy = string_copy[:-1]
    return(string == inversed_string)

#print(check_if_symmetric(s1))
#print(check_if_symmetric(s2))
#print(check_if_symmetric(s3))

#convert_to_numbers(string)
#Return an array of numbers corresponding to letters in a string where space = 0, a = 1, b = 2, and so on.
#For example, convert_to_numbers('a cat') should return [1,0,3,1,20].


def convert_to_numbers(string):
    list = []
    for letter in string:
        position = ord(letter) - 96
        list.append(position)
    return(list)

#print(convert_to_numbers(s1))
#print(convert_to_numbers(s2))
#print(convert_to_numbers(s3))


#convert_to_letters(array)
#This is the inverse of convert_to_numbers. For example, convert_to_letters([1,0,3,1,20]) should return 'a cat'.

def convert_to_letters(array):
    string = ''
    for number in array:
        letter = chr(number+96)
        string = string + letter
    return(string)

#print(convert_to_letters(convert_to_numbers(s1)))
#print(convert_to_letters(convert_to_numbers(s2)))
#print(convert_to_letters(convert_to_numbers(s3)))



#get_intersection(array1, array2)
#Return an array consisting of the elements that are in both array1 and array2. There should not be any repeated elements in the output array.
#

a1 = [1,2,3,4]
a2 = [1,'a','b',4]
def get_intersection(array1, array2):
    intersection = []
    for element in array1:
        if element in array2:
            intersection.append(element)
    return(intersection)

#print(get_intersection(a1,a2))

#get_union(array1, array2)
#Return an array consisting of the elements that are in either array1 or array2. Again, there should not be any repeated elements in the output array.
#

a1 = [1,2,3,4]
a2 = [1,'a','b',4]

def get_union(array1, array2):
    union = array1
    for element in array2:
        if element not in array1:
            union.append(element)
    
    return(union)

#print(get_union(a1,a2))


#count_characters(string)
#Count the number of each character in a string and return the counts in a dictionary. Lowercase and uppercase letters 
# should not be treated differently. For example, count_characters('A cat!!!') should return the dictionary 
# { 'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3 }.

my_string = 'cAt!!//6sda'
def count_characters(string):
    dic = {}
    string = string.lower()
    for character in string:
        if character not in dic.keys():
            dic[character] = 1
        else:
            dic[character] += 1
    return(dic)

#print(count_characters(my_string))



#is_prime(N)
#Check whether an input integer N>1 is prime by checking whether there exists some n∈{2,3,4,…,⌊N/2⌋} 
# such that n divides N. (The ⌊⌋ symbol denotes the floor function.)
N = 7
from numbers import Number
import math
def is_number(value):
    return isinstance(value, Number)
is_number(7)

def is_prime(N):
    if not is_number(N):
        raise ValueError('Must be a number!')
    if N != math.floor(N):
        raise ValueError('Must be an integer!')
    if N == 0:
        raise ValueError('Must be different from zero!')
    divisors = []
    for divisor in range(2,math.floor(N/2)+1):
        if (N%divisor)==0:
            #print(f'{N} is not a prime! {divisor} is a divisor of {N}')
            return(False)
    #print(f'{N} Is a prime!')
    return(True)

#print(is_prime(19))
##print(is_prime('a'))
#print(is_prime(10))
##print(is_prime(0))
