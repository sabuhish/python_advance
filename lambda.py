'''
lambda expression 
'''

"""
lambda, l is a lambda function that takes in a parameter called X and it returns whether x is greater than 5.
"""
l = lambda x: x > 5

# as normal fucntion we print, it takes parametr x
print(l(8))



# same as function below
def l(x):
    return x > 5

print(l(2))

def alter(values, check):
    '''
    it says create a new list which has the values of all the elements in values.
    '''
    return [val for val in values if check(val)]
    # it does same thing with filter method as above list comprehseion
    # return list(filter(check, values))

mylist_ = [1, 2, 3, 4, 5]

'''
passing in the little lambda function as our check parameter
'''

another_list = alter(mylist_, lambda x: x != 5)


# not five, succes, altering the list 5 is false
# run in python visualize tutor
print(another_list)


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

print(remove_numbers("hello5"))

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)

print(skip_letter("hello", "e"))