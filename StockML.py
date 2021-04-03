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
import logging
import http.client


def log():
    logger = logging.getLogger(__name__)  

    # set log level
    logger.setLevel(logging.DEBUG)

    # define file handler and set formatter
    file_handler = logging.FileHandler('StockML.log')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    # Logs
    #logger.debug('A debug message')
    #logger.info('An info message')
    #logger.warning('Something is not right.')
    #logger.error('A Major error has happened.')
    #logger.critical('Fatal error. Cannot continue')


def getConfig():
    with open("config.json") as config_file:
        data = json.load(config_file)
    return(data)

def main():
    log()
    print(getConfig())
    print(os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    main()