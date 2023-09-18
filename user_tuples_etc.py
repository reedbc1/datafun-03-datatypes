"""
Task 5. Tuples and More
Illustrate tuples, sets, and dictionaries in Python.

Name: Brendan Reed
Topic: Business/Finance

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
def create_tuples():
    logger.info('Calling create_tuples()')

    stock_info = ('open','close','volume','1y target est','PE ratio')
    cash_flow = ('cash received','additional cash received','expenditures','additional cash spent','total cash spent')
    employee_info = ('name','employee ID #', 'job title', 'salary', 'time at company')

    logger.info(f'{stock_info = }')
    logger.info(f'{cash_flow = }')
    logger.info(f'{employee_info = }')

# Sets: create two sets. Get the intersection and the union.
def create_sets():
    logger.info('Calling create_sets()')

    employee_names1 = {'Samantha', 'Jake', 'Brendan', 'Sophia', 'Marianne', 'Eric'}
    employee_names2 = {'David', 'Samantha', 'Lisa', 'John'}

    # set intersection
    employee_intersection = employee_names1 & employee_names2

    # set union
    employee_union = employee_names1 | employee_names2

    logger.info(f'{employee_names1 = }')
    logger.info(f'{employee_names2 = }')
    logger.info(f'{employee_intersection = }')
    logger.info(f'{employee_union = }')

# Use a dictionary to create key-value pairs of each word and its count from a file. 
# Finding count of each word in text_zen_of_python.txt
def create_dictionaries():
    logger.info('Calling create_dictionaries()')

    with open("text_zen_of_python.txt") as file_object:
        word_list = file_object.read().split()

    # creating dictionary of word counts using comprehensions (preferred approach)
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    logger.info("Given text_zen_of_python.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# call functions
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    create_tuples()
    create_sets()
    create_dictionaries()

    show_log()