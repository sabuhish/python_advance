


class Currency:
    '''
    setting two properties for all object
     and  initialize  amount to zero for 
    '''
    def __init__(self,code , exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd =exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    '''
    in_currency method should convert the amount which should be in USD to the currency stored
    in the object
    '''
    def in_currency(self, amount):
        return amount / self.exchange_to_usd


    '''
    the to us the method should do the opposite.
    Convert the amount or this parameter to USD using the exchange rate
    '''
    def to_usd(self, amount=None):
        # means if there is amount take if not go for self.amoun
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd

    """
    eqaual
    """
    def __eq__(self, other):
        return self.to_usd() == other.to_usd()

    '''
    greater than method is greater than and takes other as second args
    '''
    def __gt__(self, other):
        return self.to_usd()  > other.to_usd()

    '''
    less that
    '''
    def __lt__(self, other):
        pass
    
    '''
    less equeal
    '''
    def __le__(self, other):
        pass

    """
    greater or equal
    """
    def __ge__(self, other):
        pass


Azn = Currency("AZN", 1.72)
print(Azn.in_currency(100))
print(Azn.to_usd(100))

euros = Currency("euro", 1.95)
print(euros.in_currency(100))
print(euros.to_usd(100))

euros.set_amount(1)
print(euros.to_usd(10)) 

print(Azn > euros) #will give __gt__

'''
lambda
'''
# transform has deafult value, lamda des notuhing
def get_currence_cresource(resource, transform=(lambda x: x)):
    # imagine we getting rquest.get.. data> json
    # dictinoary takes in the list with code and amount
    data = {
        "items":[
            {"code": "usd", "amount_to_usd": 1.00},
            {"code": "gdp", "amount_to_usd": 1.21},{"code": "euro", "amount_to_usd": 1.07},{"code": "jpy", "amount_to_usd": 0.15},
        ]
    }
    '''
    accessing specifically one of the elements of that dictionary which is going to be the resource parameter.
    for example items
    '''
    my_resource = data[resource]
    # returning all of the elements inside my resource
    return [transform(x)  for x in my_resource]

# passing items, that will go to resources, down there
# resource will be data item the return each dict
currecies = get_currence_cresource("items", lambda x: x["code"].upper())

def get_currency_code():
    return  get_currence_cresource("items", lambda x: x["code"].upper())

def get_currencies():
    return get_currence_cresource("items", lambda x: Currency(x["code"], x["amount_to_usd"]))

# list of dict available currecnyies
print(get_currency_code())


print(get_currencies())

def calculate_in_all_currencies(usd_amount):
    print("--{} USD in all currencies".format(usd_amount))
    for currecy in get_currencies():
        print("In {}: {:.2f}".format(currecy.code, currecy.in_currency(usd_amount)))

calculate_in_all_currencies(1000)