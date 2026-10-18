# FINE3300 (Fall - 2026)

## Project Overview
* The purpose of this Working Directory is to provide users with a exchange rate calculator that accepts only USD, and CAD based on data sourced from Bank of Canada Exchange rates as of 1/1/2025. The Csv file from the Bank of Canada can be found In the working directory as "BankOfCanadaExchangeRate.2026.csv"
* The Human written document for the project can be found in "Exchange Rate Calculator(HUMAN).py"

### Installation Instructions

* **Unzip** the downloaded project folder.
* Open a terminal in the folder directory and ensure to install **pandas**:

### Technical Logic & Implementation 

## Creation of Exchange rate class with it's components
* Indexes data from the csv file provided for future use via pandas
* Instantiating the required variables for the method "convert"
    * Calculator Currency to, from conversion logic

## User Interface & Variables Setup
* Informs the user on the purpose of calculator and the accepted currencies
* Define the "rates" variable that will be passed through the "convert" method

## Data Processing & Parsing
* Creates three separate variables via tuple unpacking based on user input and splits the string
* Separately cleans to currency to use to fomat the final result later

## Execution & Output
* Converts the string into the desired data type while cleaning the data for any extra spaces and applies the "convert" method created earlier while making use of the already cleaned "Clean_To_Currency"
* Prints The desired result in proper formatting    