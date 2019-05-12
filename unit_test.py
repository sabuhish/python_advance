'''
test to check whatever it works or not!
'''
import unittest

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
    less than
    '''
    def __lt__(self, other):
        return self.to_usd() < other.to_usd()
    
    '''
    less equeal
    '''
    def __le__(self, other):
        return self.to_usd() <= other.to_usd()


    """
    greater or equal
    """
    def __ge__(self, other):
        return self.to_usd() >= other.to_usd()

        
# check methods if it works

# Test in name is import
class CurrencyTest(unittest.TestCase):
    '''
    So then we have this currency test class at the bottom which is a subclass of test case in inside the
    unit test package.
    '''
    # test in name is important again
    def test_create_currency(self):
        pounds = Currency("GBP", 1.21)
        # pounds.ode is gdp
        # pounds.exchnage_to_usd = 1.21

        # lets check
        self.assertEqual(pounds.code, "GBP")
        self.assertEqual(pounds.exchange_to_usd, 1.21) 
    
    def test_set_amount(self):
        pounds = Currency("GBP", 1.21)
        euros = Currency("eur", 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertEqual(pounds.amount, 5000)
        self.assertEqual(euros.amount, 10)
    
    def test_compare(self):
        pounds = Currency("GBP", 1.21)
        euros = Currency("eur", 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertTrue(pounds > euros)
        self.assertFalse(pounds < euros)
        self.assertFalse(pounds == euros)

    def test_compare_currecny_equal(self):
        pounds = Currency("GBP", 1.21)
        euros = Currency("eur", 1.21)

        pounds.set_amount(500)
        euros.set_amount(500)
        
        self.assertTrue(pounds >= euros)
        self.assertTrue(pounds <= euros)
        self.assertTrue(pounds == euros)

        self.assertFalse(pounds > euros)
        self.assertFalse(pounds < euros)

    def test_in_currency(self):
        pounds = Currency("GBP", 1.21)

        self.assertEqual(pounds.in_currency(1210), 1000)
    
    def test_to_usd(self):
        pounds = Currency("GBP", 1.21)

        self.assertEqual(pounds.to_usd(1000), 1210)
    

    def test_comparison_With_exceptions(self):
        pounds = Currency("GBP", 1.21)
        pounds.set_amount(1000)

        # this code here raised attirbute errro
        # self.assertEqual(pounds == 1000)
        with self.assertRaises(AttributeError):
            pounds == 1000