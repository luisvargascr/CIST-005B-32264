"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Western
This file is used to represent a Western Burger Object
"""

from burger import Burger


class Western(Burger):
    """Concrete class that represents a Western Burger Object."""
    def __init__(self):
        """Constructor"""
        super().__init__("Western Burger", 5.95, "Charbroiled Beef Patty, "
                                                 "Beer Battered Onion Rings, "
                                                 "Sriracha BBQ Sauce & "
                                                 "American Cheese "
                                                 "on Toasted Bun")
