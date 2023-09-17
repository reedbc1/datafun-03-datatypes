"""
Purpose: illustrating string lists

Name: Brendan Reed
Field: Business/Finance

"""

# imports first
import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define shared data ..........................................
# make 5 lists related to my area of focus (business/finance)

list_stock_tickers = ['GOOG', 'AAPL', 'FDX', 'MSFT', 'TSLA']

pays_dividends = ['no', 'yes', 'yes', 'yes', 'no']

stock_action = ['buy', 'sell', 'short', 'hold']

major_stock_exchanges_US = ['NYSE', 'NASDAQ', 'Chicago Stock Exchange']


# reusable functions next

# string lists 1: python built-in functions
# use len(), set(), and zip() to combine 2 or more lists into tuples
def string_lists1():
    logger.info("Calling string_lists1()")
    # use zip to combine 2 lists into tuples
    stock_dividends = list(zip(list_stock_tickers, pays_dividends))
    logger.info(f'stock_dividends cobmined tuples: {stock_dividends}')
    logger.info(f'stock_dividends length: {len(stock_dividends)}')
    stock_dividends_set = set(stock_dividends)
    logger.info(f'stock_dividends set: {stock_dividends_set}')

#string lists 2: random choice
# Use random.choice() to pick a random value from one of your lists.
def using_random_choice():
    logger.info("Calling using_random_choice()")
    logger.info(f'displaying random stock action from stock_action: {random.choice(stock_action)}')

# Customize the sentence generator to create random sentences about your domain. 
def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence"
    sentence = (
        f"You have decided to {random.choice(stock_action)} {random.choice(list_stock_tickers)} from {random.choice(major_stock_exchanges_US)}."
    )

    logger.info(f"Random sentence: {sentence}")

# String Lists 3. Get Unique Words
# Choose one of the text data files in the repo - or add another related your your domain.
# Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
# Sort the list. 
# Use len() to get the length display it to the console.

def process_text():
    """Read in text_hamlet.txt and process it"""
    logger.info("Calling process_text()")

    # read in hamlet to get a list of words
    with open("text_hamlet.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = sorted(set(list_words))  # remove duplicates by making a set. sorts set alphabetically.
        
        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"There are {unique_word_ct} unique words in the file.")

        # about unique words
        logger.info('One issue with the list of unique values is that many of the "unique" values are near duplicates. For example, "indeed", "indeed,", and "indeed." are all included in the list. The list could be improved by first removing punctuation and then processing the list to remove duplicates.')

# creates show_log() that will print the log to the console when called
def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# call functions and execute code
# use if __name__ == "__main__":
if __name__ == "__main__":
    logger.info("Calling functions from main block")
    string_lists1()
    using_random_choice()
    create_random_sentence()
    process_text()

    show_log()

