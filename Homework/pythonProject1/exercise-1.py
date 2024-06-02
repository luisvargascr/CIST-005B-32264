"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Description: compute_gross_pay, the following code
will prompt the user for hours and rate per hour to
compute gross pay. If the employee worked above 40
hours, the code will calculate 1.5 times the hourly rate.
ASSUMPTION: Hours are provided in whole integer numbers.
"""


def compute_gross_pay(hours: int, rate: float) -> float:
    reg_hours_per_week = 40
    additional_rate_multiplier = 1.5

    if hours > reg_hours_per_week:
        # gross pay adds extra when above 40 hours.
        gross_pay = ((hours - reg_hours_per_week) * rate * additional_rate_multiplier) + rate * reg_hours_per_week
    else:
        # otherwise, no special calculation: hours times rate for gross pay is used.
        gross_pay = hours * rate
    return gross_pay


if __name__ == "__main__":
    worked_hours = int(input("Enter Hours: "))
    hourly_rate = float(input("Enter Rate: "))
    print("Pay: %.1f" % compute_gross_pay(worked_hours, hourly_rate))

'''
Enter Hours: 56
Enter Rate: 12.25
Pay: 784.0

Enter Hours: 39
Enter Rate: 10
Pay: 390.0
'''