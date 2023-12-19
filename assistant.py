from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt

def myfunction():
  pass

mappings = {
  'greetings':myfunction
}

assistant = GenericAssistant('intents.json', intent_methods = mappings)

assistant.train_model()

assistant.request("Hello!")

portfolio = {'AAPL':20, 'TSLA':5, 'GS':10}

with open('portfolio.pkl', 'wb') as f:
  pickle.dump(portfolio, f)
  
with open('portfolio.pkl', 'rb') as f:
  portfolio = pickle.load(f)

print(portfolio)

def save_portfolio():
  with open('portfolio.pkl', 'wb') as f:
    pickle.dump(portfolio, f)

def add_portfolio():
  ticker = input("Which Stock do you want to add? ")
  amount = input("How many shares do you want to add? ")
  if ticker in portfolio.keys():
    portfolio[ticker] += amount
  else:
    portfolio[ticker] = amount
  save_portfolio()

def remove_portfolio():
  ticker = input("Which Stock do you want to sell? ")
  amount = input("How many shares do you want to sell? ")
  if ticker in portfolio.keys():
    if amount<= portfolio[ticker]:
      portfolio[ticker] -= amount
      save_portfolio()
    else:
      print("You don't have enough shares")
  else:
    print(f"You don't own any shares of {ticker}")
  
  
