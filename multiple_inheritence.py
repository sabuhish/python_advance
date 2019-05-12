class SuperBaseClass:
    def hi(self):
        print("You are here")



class ClassA(SuperBaseClass):
    '''
    if this class does not have hi method it would take superbase class method of hi
    '''
    def hi(self):
        print("Hello!")


class ClassB:
    def hi(self):
        print("Hallo!")

    def another(self):
        print("in class B.")


'''
multiple inheritence from up class
So it is the first one and in Python the way it works is whenever you try to execute a method or access
a property it will go into Class A and it will see if it's there and if it's not there the little go
into class B and see if it's there.
'''
class ClassC(ClassA, ClassB):
    pass

c =ClassC()

# definition given in the above.

'''
both below methods will look up in first inhertence if not found will move to next class object
'''
c.hi()
c.another()