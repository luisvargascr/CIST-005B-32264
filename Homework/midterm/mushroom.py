"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Mushroom
This file is used to represent a Mushroom Burger Object
"""

from burger import Burger


class Mushroom(Burger):
    """Concrete class that represents a Mushroom Burger Object."""
    def __init__(self):
        """Constructor"""
        super().__init__("Mushroom Burger", 5.95, "Beef Patty, "
                                                  "Mushrooms & Swiss Cheese, "
                                                  "Garlic Mayo, Green Leaf Lettuce, "
                                                  "& Tomato, on Toasted Bun")
