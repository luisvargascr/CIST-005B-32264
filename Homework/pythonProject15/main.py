"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/05/2024

Description: main
This file is used to test the logging class.

Create a logger object and log a raised exception in a log file (for example "newfile.log").

For example in this case:
rate = 5
percent = 0
result = rate/percent
"""

# import the logging library.
import logging

# Create and configure logger to create a newfile.log file for logging information including
# errors
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# get the instance of the logger object so we can use it
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

rate = 5
percent = 0

try:
    result = rate/percent
except Exception as e:
    print("\nException occurred: " + str(e))

    # Use of the logger object to write an exception to a log file.
    logger.error("Exception occurred: " + str(e))