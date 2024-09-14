#Write a script to decode the message 
# [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751], 
# given that it was encoded with a linear encoding function f(x)=ax+b where a and b are both integers between 0 and 100 inclusive. 
# Be sure to print out all valid messages along with the values of a and b that generated them. Note that although there may be more than 
# one valid message, only one will contain real words.

def inverse_linear_function (a,b,x):
    return((x-b)/a)


encripted_message = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]
valid_range_b = range(0,101)
valid_range_a = range(1,101)

possible_messages = []

for a in valid_range_a:
    for b in valid_range_b:
        inverse_applied = []
        for item in encripted_message:
                inverse_applied_item = inverse_linear_function(a=a,b=b,x=item)
                #print(inverse_applied_item)
                try:
                    inverse_applied_item = int(inverse_applied_item)
                    inverse_applied.append(inverse_applied_item)
                except:
                    print('nope!')
                    break
        if len(inverse_applied):
            if all((0 <= x <= 26) for x in inverse_applied): #verify it has a logical set of values
                possible_messages.append(inverse_applied)

from hello_world import convert_to_letters
for element in possible_messages:
    decrypted_message = convert_to_letters(element)
    if "`" not in decrypted_message:
        print(decrypted_message)

# is a mayonnaise aana instrument