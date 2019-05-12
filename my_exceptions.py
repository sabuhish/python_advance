'''
create your own error with inhertince 
'''

class SorryDoesNotWork(KeyError):
    pass

class NotPageExists(LookupError):
    pass

class IncorrectPassword(ValueError):
    pass

'''
this how we will raise en error messages
traceback functins raises error message will output
'''
def login():
    raise SorryDoesNotWork

try:
    login()
except SorryDoesNotWork:
    print("Sorry not the one in out database")

except IncorrectPassword:
    print("your password is wrong")