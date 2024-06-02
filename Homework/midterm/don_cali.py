"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: DonCali
This file is used to represent a DonCali Burger Object
"""

from burger import Burger


class DonCali(Burger):
    """Concrete class that represents a DonCali Burger Object."""
    def __init__(self):
        """Constructor"""
        super().__init__("DonCali Burger", 5.95, "Charbroiled Beef Patty, "
                                                 "Spring Mix Lettuce,"
                                                 "Tomato, Red Onion, "
                                                 "Avocado, Smoked Gouda & "
                                                 "Bacon on Toasted Bun")
