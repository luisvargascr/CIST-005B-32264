"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Burger
This file is used to represent a super class Burger
"""


class Burger(object):
    """Concrete class that represents a Bacon Burger Object."""

    def __init__(self, style: str = "Burger", price: float = "0.00", description: str = "Regular Burger"):
        self.name = style
        self.price = price
        self.description = description

    def __str__(self) -> None:
        """Returns the string representation of the Burger Object."""
        print("The '%s' item costs $%2.f" % (self.name, self.price))

    def getName(self) -> str:
        """Returns the name of the Burger Object."""
        return self.name

    def getPrice(self) -> float:
        """Returns the price of the Burger Object."""
        return self.price

    def getDescription(self) -> str:
        """Returns the description of the Burger Object."""
        return self.description
