"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/06/2024

Assignment: Chapter 2 - Exercise 1
File: getInputsFile.py
"""


class GetInputsFile:
    def __init__(self, companies: [str] = None):
        """
        Constructor for the class, it allows to override the list of companies
        by passing an array with company names (this is optional). If no list
        is passed, it will use the default list.
        """
        if companies:
            self.company_list = companies
        else:
            self.company_list = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

    def __get_float_val(self, variable_name: str) -> float:
        """
        This private method of the class gets a valid float input from the customer.
        It prompts for the name of the variable and returns a valid float.
        """
        if not self:
            return -1

        is_float_value_invalid = True
        float_value = 0.0
        while is_float_value_invalid:
            try:
                float_value = float(input("Enter valid %s: " % variable_name))
                is_float_value_invalid = False if float_value > 0 else True
            except ValueError:
                print("%s is invalid. Please try again." % variable_name)
                is_float_value_invalid = True
        return float_value

    def getInputs(self) -> dict:
        """
        This public method gets the actual expected inputs from the user
        such as company name, rate, and hours. It returns a dictionary
        with the keys 'rate', 'hours', and 'compan_name'.
        """
        theDict = {}
        company_name = input("Enter company name: ").strip()

        attempt = 0
        while company_name not in self.company_list:
            print("Company not in the list of companies. Please try again.")
            if attempt == 1:
                print("Valid companies are %s" % self.company_list)
                attempt = 0
            attempt += 1
            company_name = input("Enter company name: ").strip()

        rate = self.__get_float_val("Rate")
        hours = self.__get_float_val("Hours")

        theDict["rate"] = rate
        theDict["hours"] = hours
        theDict["compan_name"] = company_name

        return theDict


if __name__ == "__main__":
    inputsFile = GetInputsFile()
    my_dict = inputsFile.getInputs()
    print(my_dict)
