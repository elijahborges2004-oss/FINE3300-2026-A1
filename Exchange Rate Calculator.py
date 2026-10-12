import sys
import pandas as pd

class ExchangeRates:
    def __init__(self,CAD,USD):
        self.CAD = CAD
        self.USD = USD

        df = pd.read_csv("BankOfCanadaExchangeRate.2026.csv")
        self.Exchange_Rate=df.iloc[-1, -2]

    def converter (self,Amount,From_Currency,To_Currency):
        self.Amount = Amount
        self.From_Currency = From_Currency
        self.To_Currency = To_Currency

        if From_Currency == self.CAD and To_Currency == self.USD:
            return Amount / self.Exchange_Rate
        elif From_Currency == self.USD and To_Currency == self.CAD:
            return Amount * self.Exchange_Rate
        else:
            print("Only CAD and USD accepted")
            sys.exit()

print ("Convert to your desired currency Only USD and CAD accepted!")

rates = ExchangeRates("CAD", "USD")
amount, from_curr, to_curr = input("Enter (amount,from,to): ").split(",")
result = rates.converter(float(amount), from_curr.strip().upper(), to_curr.strip().upper())
print(f"Result: ${result:.2f}")



