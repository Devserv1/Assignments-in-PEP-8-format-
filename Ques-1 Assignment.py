#!/usr/bin/env python
# coding: utf-8

# In[22]:


#An illustrative portfolio
stock_portfolio = {
    'AAPL': {
        'shares': 50,
        'purchase_price': 120
    },
    'GOOG': {
        'shares': 100,
        'purchase_price': 150
    },
}


# In[27]:


def buy_stock(portfolio, stock_symbol, num_shares, purchase_price):
    if stock_symbol in portfolio:
        # Stock already exists in the portfolio, update the information
        present_shares = portfolio[stock_symbol]['shares']
        present_purchase_price = portfolio[stock_symbol]['purchase_price']
        total_shares = present_shares + num_shares
        average_purchase_price = ((present_shares * present_purchase_price) + (num_shares * purchase_price)) / total_shares
        portfolio[stock_symbol]['shares'] = total_shares
        portfolio[stock_symbol]['purchase_price'] = average_purchase_price
    else:
        # New stock, add it to the portfolio
        portfolio[stock_symbol] = {
            'shares': num_shares,
            'purchase_price': purchase_price
        }

    return portfolio

# Example usage:
portfolio = {
    'AAPL': {'shares': 10, 'purchase_price': 120},
    'GOOG': {'shares': 100, 'purchase_price': 150}
}
stock_symbol=input(" Stock bought:")
num_shares=input("Shares quantity bought:")
purchase_price=input(" Price:")

# Buying 20 shares of MSFT at 250 each
portfolio = buy_stock(portfolio, stock_symbol, num_shares, purchase_price)



print(portfolio)


# In[24]:


def sell_stock(portfolio, stock_symbol, num_shares_to_sell):
    if stock_symbol in portfolio:
        present_shares = portfolio[stock_symbol]['shares']
        if num_shares_to_sell <= present_shares:
            present_purchase_price = portfolio[stock_symbol]['purchase_price']
            remaining_shares = present_shares - num_shares_to_sell

            # Update the portfolio with the remaining shares
            portfolio[stock_symbol]['shares'] = remaining_shares

            # If all shares are sold, remove the stock from the portfolio
            if remaining_shares == 0:
                del portfolio[stock_symbol]

            return portfolio
        else:
            print( "Not enough shares of to sell.")
            return portfolio
    else:
        print( "You dont have this stock in portfolio")
        return portfolio



# In[25]:


import random

def calculate_portfolio_value(portfolio):
    total_portfolio_value = 0

    for stock_symbol, stock_info in portfolio.items():
        purchase_price = stock_info['purchase_price']
        random_percentage_change = random.uniform(-0.20, 0.20)
        current_price = purchase_price * (1 + random_percentage_change)
        current_value = current_price * stock_info['shares']
        total_portfolio_value += current_value

    return total_portfolio_value



# In[26]:


def portfolio_performance(initial_value, present_value):
    if initial_value == 0:
        return 0

    percentage_change = ((present_value - initial_value) / initial_value) * 100
    return percentage_change



# In[ ]:




