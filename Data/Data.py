""" Setup
Dependencies/Modules:
    json, os, pymongo

functions:
    * main - the main function of the script
"""
import os
import pymongo
import json

def log():
    logger = logging.getLogger(__name__)  

    # set log level
    logger.setLevel(logging.DEBUG)

    # define file handler and set formatter
    file_handler = logging.FileHandler('StockMLData.log')
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

def updateTickers():
    os.system('YahooTickerDownloader.py')

def main():
    log()
    return 0
if __name__ == "__main__":
    main()