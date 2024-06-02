"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: OrderManager
This file is used to represent an order manager: this is the
engine that performs calculations and provides output on screen
and text file of these calculations.
"""

import burger
from staff import Staff
from student import Student
from linked_bag import LinkedBag
from datetime import datetime


class OrderManager(object):
    """Concrete class that represents an OrderManager Object."""
    def __init__(self):
        """Constructor"""
        self.total = 0.0
        self.items = LinkedBag()
        self.order_details = {}

    @property
    def is_order_not_empty(self) -> bool:
        """Checks if order is empty (or not)."""
        return bool(self.order_details)

    def add_to_order(self, burger_item: burger, quantity: int) -> None:
        """Adds burger item and quantity to the order."""
        burger_item_name = burger_item.getName()
        if quantity == 0:
            if self.items.size > 0:
                food_item = self.items.find(burger_item_name)
                if food_item:
                    self.items.remove(food_item)
                if burger_item_name in self.order_details:
                    self.order_details.pop(burger_item_name)
        else:
            self.items.add(burger_item)
            if burger_item_name not in self.order_details:
                self.order_details[burger_item_name] = quantity
            else:
                self.order_details[burger_item_name] += quantity

    def calculate_partial_order(self) -> (str, float):
        """Calculates the cost of a partial order (without tax calculations)."""
        sub_total = 0.0
        output_text = "================================================\n"
        output_text += "Order Details:".center(25) + "\n"
        output_text += "================================================\n"
        output_text += ("%-10s %-15s %-20s\n" % ("Quantity:", "Description:", "Price:"))

        for food_item, quantity in self.order_details.items():
            current_burger = self.items.find(food_item)
            sub_total_per_item = quantity * current_burger.value.getPrice()
            sub_total += sub_total_per_item
            output_text += ("%-10d %-15s $%-3.2f USD\n" % (quantity, food_item, sub_total_per_item))

        return output_text, sub_total

    def print_partial_order(self) -> None:
        """Prints a partial order on the screen."""
        output_text, sub_total = self.calculate_partial_order()
        print(output_text)
        print("\nYour subtotal = $%.2f\n" % sub_total)

    def print_full_order(self, customer_type: int = 0, print_to_file: bool = False) -> None:
        """Prints the full customer order on the screen and if the 'print_to_file' flag is set
           to True, it will also print to a local file in the same directory as this Python script."""
        customer = None
        output_text, sub_total = self.calculate_partial_order()
        output_text += "\nYour total before taxes = $%.2f\n" % sub_total

        if customer_type == 0:
            customer = Staff()
        else:
            customer = Student()

        output_text += "Your Tax Rate = %s\n" % customer.get_tax_rate(True)
        self.total = customer.calculate_subtotal_with_sales_tax(sub_total)
        output_text += "Your total after taxes = $%.2f\n" % self.total
        output_text += "================================================\n"
        print(output_text)
        if print_to_file:
            self.__print_full_order_to_file(output_text)

    def __print_full_order_to_file(self, output_text: str) -> None:
        """Prints full customer order to a text file."""
        if self:
            time_now = datetime.now()
            file_name = time_now.strftime("Customer-Receipt-%d%m%Y%H%M%S.txt")
            receipt_file = open(file_name, 'w')
            receipt_file.write(output_text)
            receipt_file.close()
