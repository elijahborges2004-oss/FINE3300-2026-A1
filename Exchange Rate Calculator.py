import sys
import pandas as pd
# Creation of Exchange rate class with it's components
class ExchangeRates:
    def __init__(self,CAD,USD):
        self.CAD = CAD
        self.USD = USD

        # Indexs data from the csv file provided for future use via pandas
        df = pd.read_csv("BankOfCanadaExchangeRate.2026.csv")
        self.Exchange_Rate=df.iloc[-1, -2]

    # Instantiating the required variables for the method "convert"
    def convert (self,Amount,From_Currency,To_Currency):
        self.Amount = Amount
        self.From_Currency = From_Currency
        self.To_Currency = To_Currency
        # Calculator Currency to, from conversion logic
        if From_Currency == self.CAD and To_Currency == self.USD:
            return Amount / self.Exchange_Rate
        elif From_Currency == self.USD and To_Currency == self.CAD:
            return Amount * self.Exchange_Rate
        else:
            print("Only CAD and USD accepted")
            sys.exit()
# Informs the user on the purpose of calculator and the accepted currencies
print ("Convert to your desired currency Only USD and CAD accepted! e.g (144,USD,CAD)")
# Define the "rates" variable that will be passed through the "convert" method
rates = ExchangeRates("CAD", "USD")
# Creates three seperate variables via tuple unpacking based on user input and splits the string
amount, From_Currency, To_Currency = input("Enter (amount,from,to): ").split(",")

#Seperately cleans to currency to use to fomat the final result later
Clean_To_Currency = To_Currency.strip().upper()
'''
Converts the string into the desired data type while cleaing the data for any extra spaces
and applies the "convert" method created earlier while making use of the already cleaned "Clean_To_Currency"
'''
result = rates.convert(float(amount), From_Currency.strip().upper(), Clean_To_Currency)
# Prints The desired result in proper formatting
print(f"Result: ${result:.2f} {Clean_To_Currency}")