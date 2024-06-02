"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/06/2024

Description: This program asks the user to enter their company name to
validate it based on the database list(COMPANYLIST).
If the user enters invalid inputs (which means it is not in the database
list), after the second invalid input, your code should show (print)
the list of the company names.

#company database list
COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

Ask the user the rate and the hours and validate them to be a numeric
and positive value. Save the inputs in a dictionary like
theDict = { "rate":50, "hours": 120, "compan_name": "Google"}
If "hours" is greater than 40, multiply 1.5 by the rate for the overtime
print the pay stub
Use modules and import them to the main file

Assignment: Chapter 2 - Exercise 1
File: chapter-2-exercise-1.py
Dependencies:
1) computePayFile.py
2) getInputsFile.py
3) printPayFile.py
"""

from getInputsFile import GetInputsFile
from computePayFile import ComputePayFile
from printPayFile import PrintPayFile


def payProcess():
    """
    This function is to process all other functions to get inputs,
    calculate and print the pay stub
    """
    my_inputs = GetInputsFile().getInputs()
    ComputePayFile().computePay(my_inputs.get("rate"), my_inputs.get("hours"), my_inputs)
    PrintPayFile().printPay(my_inputs)


if __name__ == '__main__':
    payProcess()

"""
Example Output #1:
------------------

Enter company name: Intel
Company not in the list of companies. Please try again.
Enter company name: AMD
Company not in the list of companies. Please try again.
Valid companies are ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
Enter company name: Facebook
Enter valid Rate: -1
Enter valid Rate: 95.75
Enter valid Hours: 0
Enter valid Hours: 42
For company 'Facebook', the provided rate was $95.75 USD and the hours were 42.0. Therefore, the total gross pay was $4117.25 USD.

Example Output #2:
------------------

Enter company name: Apple
Enter valid Rate: 125.25
Enter valid Hours: 40
For company 'Apple', the provided rate was $125.25 USD and the hours were 40.0. Therefore, the total gross pay was $5010.0 USD.

Example Output #3:
------------------

Enter company name: Uber
Enter valid Rate: 789
Enter valid Hours: 41
For company 'Uber', the provided rate was $789.0 USD and the hours were 41.0. Therefore, the total gross pay was $32743.5 USD.

"""
