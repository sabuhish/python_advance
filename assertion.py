



def divide(number, divide):
    if divide == 0:
        raise ValueError("Cant be 0 in python!")
        
    return number / divide

def divide_1(number, divide):
    '''
    assert divisor is not equal to zero.
    this does is exactly the same thing in the above
    It will check whether divisor is 0 and if it is zerothen it will raise an assertion error.
    '''
    assert divide != 0, "Divided a number by zero"
    return number / divide
# use assertion when values are gonna be incorrect
print(divide_1(2,0))
print(divide(2,0))