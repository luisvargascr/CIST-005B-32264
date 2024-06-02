"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Bacon
This file is used to represent a Bacon Burger Object
"""

from burger import Burger


class Bacon(Burger):
    """Concrete class that represents a Bacon Burger Object."""
    def __init__(self):
        """Constructor"""
        super().__init__("Bacon Burger", 5.75, "Charbroiled Beef Patty, "
                                               "Smoked Bacon, "
                                               "Caramelized Onion &"
                                               "American Cheese "
                                               "on Toasted Bun")
