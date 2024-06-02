"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Order
This file is used to represent an order system
"""

from bacon import Bacon
from deanza import DeAnza
from don_cali import DonCali
from mushroom import Mushroom
from western import Western
from order_manager import OrderManager


class Order(object):
    """Concrete class that represents an Order Object."""
    exit_option = 6

    def __init__(self, title: str = ""):
        """Constructor"""
        self.order_manager = OrderManager()
        self.menu_title = title
        self.menu_items = {1: DeAnza(),
                           2: Bacon(),
                           3: Mushroom(),
                           4: Western(),
                           5: DonCali()}

    def show_main_menu(self) -> None:
        """Shows the main menu to the customer on the screen."""
        print("======================================")
        print("Welcome to %s" % self.menu_title)
        print("======================================")
        print("Food Menu:".center(25))
        print("--------------------------------------")
        print("%-5s %-15s %-20s" % ("Option:", "Description:", "Price:"))
        print("--------------------------------------")
        for item_number, value in self.menu_items.items():
            print("%-7d %-15s $%-3.2f USD" % (item_number, value.getName(), value.getPrice()))
        print("%-7d %-15s" % (6, "Exit"))
        print("======================================")

    def take_and_process_customer_order(self, show_item_details: bool = False) -> None:
        """Method that takes the order details from the customer and processes that order."""
        keep_asking_customer_for_input = True

        while keep_asking_customer_for_input:
            menu_item = self.ask_menu_item(self.exit_option)
            if menu_item == self.exit_option:
                keep_asking_customer_for_input = False
                if self.order_manager.is_order_not_empty:
                    customer_type = self.ask_customer_type()
                    self.order_manager.print_full_order(customer_type, True)
                print("\nThank you, hope to see you again!")
            else:
                if show_item_details:
                    print("- Item Name:", self.menu_items[menu_item].getName())
                    print("- Item Description:", self.menu_items[menu_item].description)
                menu_item_quantity = self.ask_item_quantity()
                self.order_manager.add_to_order(self.menu_items[menu_item], menu_item_quantity)
                self.order_manager.print_partial_order()

    def ask_customer_type(self) -> int:
        """Method that asks the customer if they are student or staff for discount calculations."""
        customer_type = 0
        if not self:
            return customer_type
        try:
            customer_type = int(input("Please enter 1 if 'Student' or hit enter for 'Staff' and others: "))
        except ValueError:
            print("\n* No special discount *\n")

        return customer_type

    def ask_menu_item(self, exit_option: int) -> int:
        """Method that asks the customer to enter the option from the menu they want to order."""
        is_menu_option_valid = True
        selected_option = 0
        while is_menu_option_valid:
            try:
                selected_option = int(input("Please enter your option: ").strip())
                if selected_option == exit_option:
                    is_menu_option_valid = False
                else:
                    is_menu_option_valid = self.is_menu_selection_invalid(selected_option)

            except ValueError:
                print("\n*** Invalid option. Please enter 1-5 with option 6 to exit. ***\n")

        return selected_option

    def is_menu_selection_invalid(self, option: int) -> bool:
        """Method that checks the validity of the menu option selected by the customer."""
        if option not in self.menu_items:
            print("\n*** Invalid option. Please enter 1-5 with option 6 to exit. ***\n")
            return True
        else:
            return False

    def ask_item_quantity(self) -> int:
        """Method that asks the customer the quantity of items per item."""
        if not self:
            return 0

        is_quantity_valid = True
        quantity = 0
        while is_quantity_valid:
            try:
                quantity = int(input("Please enter how many items you want (0 to remove): ").strip())
                is_quantity_valid = self.is_quantity_invalid(quantity)
            except ValueError:
                print("Invalid value. Please enter 0 to cancel the previous item or enter a valid number of items.")

        return quantity

    def is_quantity_invalid(self, quantity: int) -> bool:
        """Method that checks that the quantity entered by the user is valid."""
        if not self or quantity < 0:
            print("\n*** Invalid option. Please enter 0 to clear the item or a positive number to request the item."
                  "***\n")
            return True
        else:
            return False
