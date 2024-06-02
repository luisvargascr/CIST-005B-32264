"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: DeAnza
This file is used to represent a DeAnza Burger Object
"""

from burger import Burger


class DeAnza(Burger):
    """Concrete class that represents a DeAnza Burger Object."""
    def __init__(self):
        """Constructor"""
        super().__init__("DeAnza Burger", 5.25, "Charbroiled Beef Patty, "
                                                "Green Leaf, Tomato, "
                                                "Red Onion, "
                                                "White Cheddar on Toasted Bun")
