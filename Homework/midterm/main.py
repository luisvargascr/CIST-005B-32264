"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: This is the entry point to the program.
Consider this file "main" and where execution should start.
"""

from order import Order

if __name__ == "__main__":
    my_main_order_system = Order("De Anza College Food Court")
    my_main_order_system.show_main_menu()
    my_main_order_system.take_and_process_customer_order()

# SAMPLE OUTPUTS DOWN BELOW - PLEASE CHECK BELOW FOR OUTPUT EXAMPLES...
# OUTPUT EXAMPLE 1:
'''
======================================
Welcome to De Anza College Food Court
======================================
        Food Menu:       
--------------------------------------
Option: Description:    Price:              
--------------------------------------
1       DeAnza Burger   $5.25 USD
2       Bacon Burger    $5.75 USD
3       Mushroom Burger $5.95 USD
4       Western Burger  $5.95 USD
5       DonCali Burger  $5.95 USD
6       Exit           
======================================
Please enter your option: a

*** Invalid option. Please enter 1-5 with option 6 to exit. ***

Please enter your option: -7

*** Invalid option. Please enter 1-5 with option 6 to exit. ***

Please enter your option: 1
Please enter how many items you want (0 to remove): b
Invalid value. Please enter 0 to cancel the previous item or enter a valid number of items.
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD


Your subtotal = $5.25

Please enter your option: 6
Please enter 1 if 'Student' or hit enter for 'Staff' and others: 

* No special discount *

================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD

Your total before taxes = $5.25
Your Tax Rate = 9.0%
Your total after taxes = $5.72
================================================


Thank you, hope to see you again!'''

# OUTPUT EXAMPLE 2

'''======================================
Welcome to De Anza College Food Court
======================================
        Food Menu:       
--------------------------------------
Option: Description:    Price:              
--------------------------------------
1       DeAnza Burger   $5.25 USD
2       Bacon Burger    $5.75 USD
3       Mushroom Burger $5.95 USD
4       Western Burger  $5.95 USD
5       DonCali Burger  $5.95 USD
6       Exit           
======================================
Please enter your option: 1
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD


Your subtotal = $5.25

Please enter your option: 2
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD


Your subtotal = $11.00

Please enter your option: 6
Please enter 1 if 'Student' or hit enter for 'Staff' and others: 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD

Your total before taxes = $11.00
Your Tax Rate = No Sales Tax for Students!
Your total after taxes = $11.00
================================================


Thank you, hope to see you again!'''

# EXAMPLE OUTPUT 3

'''
======================================
Welcome to De Anza College Food Court
======================================
        Food Menu:       
--------------------------------------
Option: Description:    Price:              
--------------------------------------
1       DeAnza Burger   $5.25 USD
2       Bacon Burger    $5.75 USD
3       Mushroom Burger $5.95 USD
4       Western Burger  $5.95 USD
5       DonCali Burger  $5.95 USD
6       Exit           
======================================
Please enter your option: 1
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD


Your subtotal = $5.25

Please enter your option: 2
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD


Your subtotal = $11.00

Please enter your option: 3
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD
1          Mushroom Burger $5.95 USD


Your subtotal = $16.95

Please enter your option: 4
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD
1          Mushroom Burger $5.95 USD
1          Western Burger  $5.95 USD


Your subtotal = $22.90

Please enter your option: 5
Please enter how many items you want (0 to remove): 1
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
1          Bacon Burger    $5.75 USD
1          Mushroom Burger $5.95 USD
1          Western Burger  $5.95 USD
1          DonCali Burger  $5.95 USD


Your subtotal = $28.85

Please enter your option: 2
Please enter how many items you want (0 to remove): 3
================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
4          Bacon Burger    $23.00 USD
1          Mushroom Burger $5.95 USD
1          Western Burger  $5.95 USD
1          DonCali Burger  $5.95 USD


Your subtotal = $46.10

Please enter your option: 6
Please enter 1 if 'Student' or hit enter for 'Staff' and others: 

* No special discount *

================================================
      Order Details:     
================================================
Quantity:  Description:    Price:              
1          DeAnza Burger   $5.25 USD
4          Bacon Burger    $23.00 USD
1          Mushroom Burger $5.95 USD
1          Western Burger  $5.95 USD
1          DonCali Burger  $5.95 USD

Your total before taxes = $46.10
Your Tax Rate = 9.0%
Your total after taxes = $50.25
================================================


Thank you, hope to see you again!'''