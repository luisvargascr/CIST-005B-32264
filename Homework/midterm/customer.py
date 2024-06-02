"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Customer
This file is used to represent a Customer Abstract Class.
Concrete classes that use this class must implement the methods listed below.
"""

from abc import ABC, abstractmethod


class Customer(ABC):
    @classmethod
    @abstractmethod
    def calculate_subtotal_with_sales_tax(cls, sub_total: float = 0.0) -> float:
        """Returns the subtotal price of an order with the sales tax based on customer type."""
        pass

    @classmethod
    @abstractmethod
    def get_tax_rate(cls, human_readable: bool = False) -> float | str:
        """Returns either the numeric or human-readable sales tax value for the customer."""
        pass
