'''
Required variables for the currency converter class
Canadian Dollar, US Dollar, and exchange rate, date
'''

import pandas as pd
df = pd.read_csv('BankOfCanadaExchangeRate.2026.csv')
df

class ExchangeRates:
    def __init__(self, CAD_Dollar, US_Dollar, exchange_rate, date):
        self.Canadian_Dollar = CAD_Dollar
        self.US_Dollar = US_Dollar
        self.exchange_rate = exchange_rate
        self.date = date