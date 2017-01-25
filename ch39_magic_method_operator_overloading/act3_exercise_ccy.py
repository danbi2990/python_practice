"""

The class "Ccy" can be used to define money values in various currencies. A Ccy instance has the string attributes 'unit' (e.g. 'CHF', 'CAD' od 'EUR' and the 'value' as a float. 
A currency object consists of a value and the corresponding unit.



"""
import urllib.request   


def get_currencies(base="EUR"):
    """ downloads latest exchange rates """
    currency_dict = {}
    for currency in ("EUR", "USD", "GBP", "CHF", "CAD", "JPY"):
        url = 'http://finance.yahoo.com/d/quotes.csv?&s=' + currency + '=X&f=p'
        currency_dict[currency] = float(urllib.request.urlopen(url).read())
    factor = currency_dict[base]
    for currency in currency_dict:
        currency_dict[currency] /= factor
    return currency_dict

class Ccy:
    currencies = get_currencies()

    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def __repr__(self):
        return 'Ccy(' + str(self.value) + ', "' + self.unit + '")'

    def changeTo(self, new_unit):
        """
        An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
        Defines the '+' operator.
        If other is a CCy object the currency values 
        are added and the result will be the unit of 
        self. If other is an int or a float, other will
        be treated as a Euro value. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        return Ccy(x + self.value, self.unit)

    def __iadd__(self, other):
        """
        Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res

    # __sub__, __isub__ and __rsub__ can be defined analogue


    def __mul__(self, other):
        """
        Multiplication is only defined as a scalar multiplication, 
        i.e. a money value can be multiplied by an int or a float.
        It is not possible to multiply to money values
        """
        if type(other) == int or type(other) == float:
            return Ccy(self.value * other, self.unit)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if type(other) == int or type(other) == float:
            self.value *= other
            return self
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)

if __name__ == "__main__":
    x = Ccy(10.00, "EUR")
    y = Ccy(10.00, "GBP")
    print(x + y)
    # Ccy(21.215104685942173, "EUR")
    print(x + y)
    # 21.22 EUR
    print(2 * x + y * 0.9)
    # 30.09 EUR

    x = Ccy(1000, "JPY")
    y = Ccy(10, "CHF")
    z = Ccy(15, "CAD")
    print(2 * x + 4.11 * y + z)
    # 7722.98 JPY

    a = 12
    print(type(a).__name__)
