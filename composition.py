'''
Composition what you would expect a class to be composed of other classes.
'''

class Leg:
    pass

class Back:
    pass

class Chair:
    '''
    chair is gonna have number of legs
    composed Chair out of two classes LEG and BACK
    we dont use inheritence here, 
    we use inheritence when child is parent.
    Chair is not Leg or Back. it contains Chair or back
    competition is it is  making up one class out of many other classes.
    '''
    def __init__(self, num_legs):
        self.legs = [Leg() for leg in range(num_legs)]
        self.back = Back()
    
    def __repr__(self):
        return "i have {} legs ve bir back".format(len(self.legs))
    
print(Chair(5))