

class Decimal:
    '''
    define init method and here  put in the number and also the places
    '''
    def __init__(self, number, places):
        self.number = number
        self.places = places
    '''
    print a object of this class we are going to do so using the repr method
    format to print out floating point numbers. 15.68
    number of them are places and the F is for floating point
    '''
    def __repr__(self):
        #return "%.2f" % self.number #old version
        return "%.{}f".format(self.places) % self.number

    def add(self):
        pass

'''
when we print repr method is going to called
15.68
'''
print(Decimal(15.6789,3))

'''
Currency inherits from Decimal
currently it does nothings 
Except it does everything that the decimal class does.
That's what inheritance it's all of the things.
Decimal can do. properties methods from it.
inheritance is just like in nature.
'''
class Currency(Decimal):
    '''
    this class currency has superclass a parent class.
    it's getting the superclass which is decimal and it's calling the init method
    '''
    def __init__(self,symbol, number, places):
        super().__init__(number, places)
        self.symbol = symbol

    '''
    symbol does not write so lets overwtite it.
    that calls symbol and super class
    superclasses repr method, uses self places and numbers, calling class repr in the up
    '''
    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())

    # this method of Currency not Decimal
    def add_currency(self, currency):
        #exchagne between currencies
        pass

print(Currency("$",15.6789,3))

