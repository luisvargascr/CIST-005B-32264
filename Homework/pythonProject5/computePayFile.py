"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/06/2024

Assignment: Chapter 2 - Exercise 1
File: computePayFile.py
"""


class ComputePayFile:
    def computePay(self, rate: float, hours: float, dictionary: dict = None) -> float:
        """
        This public method computes the pay rate by receiving a rate and number of hours.
        Optionally, it accepts a dictionary and returns 'gross_pay' as the key and
        the result of the calculation as the value for that key. Always returns
        the calculation as a float.
        """
        if not self:
            return -1
        reg_hours_per_week = 40
        additional_rate_multiplier = 1.5

        if hours > reg_hours_per_week:
            # gross pay adds extra when above 40 hours.
            gross_pay = ((hours - reg_hours_per_week) * rate * additional_rate_multiplier) + rate * reg_hours_per_week
        else:
            # otherwise, no special calculation: hours times rate for gross pay is used.
            gross_pay = hours * rate

        if dictionary:
            dictionary["gross_pay"] = gross_pay

        return gross_pay


if __name__ == "__main__":
    pay_calculator = ComputePayFile()
    pay_amount = pay_calculator.computePay(50.25, 60.5)
    print("Test for pay with rate at $50.25 USD and hours at 60.50 is $%.2f USD per month." % pay_amount)
