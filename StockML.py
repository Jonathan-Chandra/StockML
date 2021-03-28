""" StockAI

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

Dependencies/Modules:
    json

functions:
    * main - the main function of the script
"""
import json
import os
import alpaca_trade_api as trade_api

def getConfig():
    with open("config.json") as config_file:
        data = json.load(config_file)
    return(data)

def main():
    config = getConfig()
    print(config)

if __name__ == "__main__":
    main()