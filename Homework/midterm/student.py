"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Student
This file is used to represent customer who is a member of the student body:
this allows for student customers to have specific sales tax calculations
"""

from customer import Customer


class Student(Customer):
    __tax_rate = 0.0

    def __init__(self):
        """Constructor"""
        super().__init__()

    @classmethod
    def calculate_subtotal_with_sales_tax(cls, sub_total: float = 0.0) -> float:
        """Calculates the subtotal of a sale for a student customer (students pay no sales tax)."""
        return sub_total

    @classmethod
    def get_tax_rate(cls, human_readable: bool = False) -> float | str:
        """Gets the rate of sales tax for a student customer. It returns a human-readable
        message about not having to pay sales tax or the numeric and effective sales tax rate at 0."""
        if human_readable:
            return "No Sales Tax for Students!"
        else:
            return cls.__tax_rate
