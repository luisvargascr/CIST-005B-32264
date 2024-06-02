"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Staff
This file is used to represent customer who is a member of the staff:
this allows for staff customers to have specific sales tax calculations
"""

from customer import Customer


class Staff(Customer):
    __tax_rate = 0.09

    def __init__(self):
        """Constructor"""
        super().__init__()

    @classmethod
    def calculate_subtotal_with_sales_tax(cls, sub_total: float = 0.0) -> float:
        """Calculates the subtotal of a sale, including sales taxes, for a staff customer."""
        return (sub_total * cls.__tax_rate) + sub_total

    @classmethod
    def get_tax_rate(cls, human_readable: bool = False) -> float | str:
        """Gets the rate of sales tax for a staff customer. It returns either the human-readable
        for or the numeric form of the tax rate for that staff customer."""
        if human_readable:
            return str(cls.__tax_rate * 100) + "%"
        else:
            return cls.__tax_rate
