"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop

Description: compute_gross_pay, the following code
will prompt the user for hours and rate per hour to
compute gross pay. If the employee worked above 40
hours, the code will calculate 1.5 times the hourly rate.

Exercise # 2
"""
from random import randint


def compute_gross_pay(hours: float, rate: float) -> float:
    reg_hours_per_week = 40
    additional_rate_multiplier = 1.5

    if hours > reg_hours_per_week:
        # gross pay adds extra when above 40 hours.
        gross_pay = ((hours - reg_hours_per_week) * rate * additional_rate_multiplier) + rate * reg_hours_per_week
    else:
        # otherwise, no special calculation: hours times rate for gross pay is used.
        gross_pay = hours * rate
    return gross_pay


def check_if_integer(number) -> bool:
    if number == int(number):
        return True
    else:
        return False


if __name__ == "__main__":
    invalid_input = True
    company_name = input("Enter your company name: ")

    while invalid_input:
        try:
            worked_hours = float(input("Enter the hours: ").strip())
            hourly_rate = float(input("Enter the rate: ").strip())

            invalid_input = False

            print("Company: %s" % company_name)

            # convert = lambda x: (int(x), "d") if x == int(x) else (x, ".2f")

            str_worked_hours = str(worked_hours) if check_if_integer(worked_hours) else str(("%.2f", worked_hours))
            str_hourly_rate = str(hourly_rate) if check_if_integer(hourly_rate) else str(("%.2f", hourly_rate))

            print("hours: %s" % str_worked_hours)
            print("Rate: %s" % str_hourly_rate)
            print("**********************************************")
            print("Your document number is: %s" % str(randint(1000, 2000)))

            float_pay = compute_gross_pay(worked_hours, hourly_rate)
            str_gross_pay = str(float_pay) if check_if_integer(float_pay) else str(("%.2f", float_pay))

            print("Your %s gross pay is %s" % (company_name, str_gross_pay))

        except ValueError:
            invalid_input = True
            print("Error, please enter numeric input")

'''
Sample output 1:
----------------

Company: Google
hours: 56
Rate: 12.25
**********************************************
Your document number is: 1835
Your Google gross pay is 784 dollars.

Sample output 2:
----------------
Company: Meta
hours: 60
Rate: 22.75
**********************************************
Your document number is: 1693
Your Meta gross pay is 1592.5 dollars. ==> 25.75, 30, 25.50

Sample output 3:
---------------
Enter your company name: AMD
Enter the hours: forty
Error, please enter numeric input
Enter the hours: sixty
Error, please enter numeric input
Enter the hours: 40
Enter the rate: 66.2547
Company: AMD
hours: 40
Rate: 66.25
**********************************************
Your document number is: 1365
Your AMD gross pay is 2650.19 dollars.

'''
