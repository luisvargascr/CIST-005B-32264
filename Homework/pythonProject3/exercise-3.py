"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop

Description: The following code
will prompt the user for hours and rate per hour to
compute gross pay. If the employee worked above 40
hours, the code will calculate 1.5 times the hourly rate.

Code is broken down into three functions:

1) get_input => validates inputs to ensure they are numeric and returns 2 values, the rate and the hours.
2) compute_pay => gets the 2 values, the rate and the hours, and will return the pay.
3) print_output=> gets the pay and will print it.

Exercise # 3
"""


def get_input() -> (float, float):
    invalid_input = True
    worked_hours, hourly_rate = 0, 0

    while invalid_input:
        try:
            worked_hours = float(input("Enter Hours: ").strip())
            hourly_rate = float(input("Enter Rate: ").strip())

            invalid_input = False

        except ValueError:
            invalid_input = True
            print("Error, please enter numeric input")

    return worked_hours, hourly_rate


def compute_pay(hours: float, rate: float) -> float:
    reg_hours_per_week = 40
    additional_rate_multiplier = 1.5

    if hours > reg_hours_per_week:
        # gross pay adds extra when above 40 hours.
        gross_pay = ((hours - reg_hours_per_week) * rate * additional_rate_multiplier) + rate * reg_hours_per_week
    else:
        # otherwise, no special calculation: hours times rate for gross pay is used.
        gross_pay = hours * rate
    return gross_pay


def print_output(pay: float) -> None:
    print("Pay 1: %.2f" % pay)
    print("Pay 2: %g" % pay)
    # 50.00 ==> 50.
    # 50.5  ==> 50.50



def main() -> None:
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)


if __name__ == "__main__":
    main()
