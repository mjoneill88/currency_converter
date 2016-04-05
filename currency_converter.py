
class Currency:
    def __init__(self, amount, currency_code):
        self.amount=amount
        self.currency_code=currency_code

    def __eq__(self, other):
        return self.amount==other.amount and self.currency_code==other.currency_code

    def __ne__(self, other):
        return self.amount!=other.amount and self.currency_code!= other.currency_code

    def __lt__(self, other):
        return self.amount < other.amount and self.currency_code < other.currency_code

    def __gt__(self, other):
        return self.amount > other.amount and self.currency_code == other.currency_code

    def __le__(self, other):
        return self.amount <= other.amount and self.currency_code == other.currency_code

    def __ge__(self, other):
        return self.amount >= other.amount and self.currency_code >= other.currency_code

    def __add__(self, other):
        if self.currency_code==other.currency_code:
            return Currency(self.amount+other.amount, self.currency_code)

    def __str__(self):
        return str(self.amount) + (' ') + (self.currency_code)

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)





one_dollar=Currency(1, 'MEX')

two_dollars=Currency(2,'MEX')

three_dollar=one_dollar + two_dollars

print(one_dollar)
print(two_dollars)
print(three_dollar)












#class Dollar(Currency):
#    def __init__(self, amount, currency_code='USD',):
#        self.amount=amount
