
# AttributeError:

class Myclass:
    pass

'''
AttributeError: 'Myclass' object has no attribute 'my_property'
'''
x  = Myclass()
# x.my_property

class MyClass_2:
    def __init__(self):
        self.my_property = 5
# this will work easily beacsue it has property of class
new = MyClass_2()
print(new.my_property)

# ImportError

# import my_module

# KeyError

my_dict = {"x":5, "y": 4}
# this will raise keyerror for not having key of z
# print(my_dict["z"])

# RunTimeError
'''
TypeError
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
code below, wrong type
'''
# int([])
'''
ValueError
ValueError: invalid literal for int() with base 10: 'a'
'''
# int("a")
int(2)

'''
IOError
when file did not found
FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
'''

open("my_file.txt", "r")