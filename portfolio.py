"""

Let's first start, following Ned's example, by creating a type representing a stock portfolio.
Create a file in your repository called portfolio.py by using VSCode from GitHub Desktop, as we did a few weeks ago.
Within it, define a new class called Portfolio which:
has a method called buy, which adds a new stock to the portfolio, taking 3 arguments
name, a str, the symbol of the stock which is being bought
shares, an int, the quantity which is being bought
price, a float, the price paid per share
and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio
Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere. You may do so by any means convenient to you.

"""
class Shares:
    def __init__(self,name,number,price):
        self.name = name 
        self.number=number
        self.price=price

class Portfolio:
    def __init__(self):
        self.stocks=[]
    def buy(self,shares):
        self.stocks.append(shares)

    def cost(self):
        return sum(shares.number * shares.price for shares in self.stocks)