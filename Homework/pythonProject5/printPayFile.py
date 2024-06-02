"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/06/2024

Assignment: Chapter 2 - Exercise 1
File: printPayFile.py
"""


class PrintPayFile:
    def printPay(self, pay_dict: dict) -> None:
        """
        This public method receives a dictionary and prints the values of the dictionary.
        However, the dictionary is expected to have the following keys: 'compan_name',
        'rate', 'hours', and 'gross_pay' to be able to print any results.
        """
        if not self:
            return
        if not pay_dict:
            print("No payment information was provided. Exiting.")
            return

        if "compan_name" not in pay_dict or \
                "rate" not in pay_dict or "hours" not in pay_dict or "gross_pay" not in pay_dict:
            print("Your dictionary of company and hour/rate information is formatted incorrectly.")
            return

        print("For company '%s', the provided rate was $%s USD and the hours were %s. Therefore, the total "
              "gross pay was $%s USD." \
              % (pay_dict.get("compan_name", "NO VALUE PROVIDED"), round(pay_dict.get("rate", -1), 2),
                 round(pay_dict.get("hours", -1), 2), round(pay_dict.get("gross_pay", -1), 2)))


if __name__ == "__main__":
    printFile = PrintPayFile()
    theDict = {"rate": 50.25, "hours": 120.2254, "compan_name": "Google", "gross_pay": 1236}
    printFile.printPay(theDict)
