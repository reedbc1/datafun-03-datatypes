"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import random
import statistics

# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [71, 10, 89, 92, 78, 16, 98, 87, 47, 26, 42, 58, 78, 51, 52, 10, 23, 69, 87, 35]

# time range
listx = list(range(1,11))

# amount of stock traded
listy = [1050, 1251, 5556, 4902, 5314, 3437, 3297, 5313, 3286, 5076]

# TODO: define some custom functions

# finding descriptive statistics for list1
def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"list1: {list1}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")

# for listx and listy: calculating correlation and predicting future values with linear regression
def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy}")

    # Predictive: Machine Learning - Linear Regression
    # If the corrlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(listx)
    newx = x_max * 1.5  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info("We predict that when x = {newx}, y will be about {newy}")

# using python built-in functions
def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list1}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )

# illustrating list methods
def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = [30, 40, 55, 71, 5, 30]
    lst.append(87)

    # extend the list with another list
    lst.extend([33, 99, 11])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 101
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 5
    lst.remove(item_to_remove)

    # Count how many times 111 appears in the list
    ct_of_30 = lst.count(30)

    # Sort the list in ascending order using the sort() method
    asc_lst = lst.sort()

    # Sort the list in descending order using the sort() method
    desc_lst = lst.sort(reverse=True)

    # Copy the list to a new list
    new_lst = lst.copy()
    logger.info(f"new_lst is: {new_lst}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_lst.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_lst}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_lst.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_scores is: {new_lst}"
    )

    # Remove the item at index 3 from the new list
    fourth = new_lst.pop(3)
    logger.info(
        f"Popped the fourth (index=3): {fourth} and now, new_scores is: {new_lst}"
    )


def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("list1: {list1}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filtering to only store even values in a list
    even_values = [filter(lambda x: x % 2 == 0, list1)]
    logger.info(f"Even values: {even_values}")

    # Use the built-in function map() anywhere you need to transform a list

    # mapping each x to the cuberoot of x
    cuberoot = [map(lambda x: math.pow(x, 1/3), list1)]
    logger.info(f"Doubled scores: {cuberoot}")

    # using map to find the volume of a cube with a side length equal to the value of each list element
    # creating a list with smaller values so values are not astronomically large
    new_list = [14, 7, 4, 5, 8]
    new_list_cubed = [map(lambda x: math.pow(x, 3), new_list)]
    logger.info(f"Cubed values: {new_list_cubed}")

# Lists 6. List Transformations - Using List Comprehension 
def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("list1: {list1}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    # making a new list of values under 3000
    values_under_3000 = [x for x in list1 if x < 3000]
    logger.info("Values under 3000 (using list comprehensions!): {values_under_3000}")

    # making a new list where each value is tripled
    triple_values = [x * 3 for x in list1]
    logger.info("values tripled: {triple_values}")

    # my own transformation
    # making a new list that displays the square root of each value where the original value was less than 2500
    sqrt_less_than_1000 = [x * (1/2) for x in list1 if x < 2500]
    logger.info("square root of each values less than 2500: {doubled_scores}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    show_log()



