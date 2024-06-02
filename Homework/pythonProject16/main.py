"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/12/2024

Description: main
Write the pay calculation using annotations for the function(s) and the parameters.

(no need to check the user inputs for this exercise)

pay = hours * rate

get input function
calculate function
print function
Also, use "__annotations__" to print the annotations for your functions.

"""


def get_input_from_user() -> (float, float):
    """ This function gets the input from the user and returns the number of hours worked
        and the rate per hour provided by the user. """

    print("*********** Please enter information to calculate pay below ************\n")
    number_of_hours = float(input("Enter Hours: "))
    rate_per_hour = float(input("Enter Hourly Rate: "))
    return number_of_hours, rate_per_hour


def calculate_pay(hours: float, rate: float) -> float:
    """ This function takes the number of hours worked and the rate per hour and calculates
        pay accordingly. The returned value is the total pay. """
    reg_hours_per_week = 40
    additional_rate_multiplier = 1.5

    if hours > reg_hours_per_week:
        # gross pay adds extra when above 40 hours.
        gross_pay = ((hours - reg_hours_per_week) * rate * additional_rate_multiplier) + rate * reg_hours_per_week
    else:
        # otherwise, no special calculation: hours times rate for gross pay is used.
        gross_pay = hours * rate
    return gross_pay


def print_pay_results(hours: float, rate: float, gross_pay: float) -> None:
    """ This function takes the hours worked, the hourly rate, and the gross pay and prints
        them on the screen. """
    print("The gross pay for %.0f hours of work at $%.2f rate is $%.2f USD.\n" % (hours, rate, gross_pay))


def print_annotations() -> None:
    print("-----------------------Annotations Information:--------------------------")
    print("For 'get_input_from_user()' function: %s" % get_input_from_user.__annotations__)
    print("For 'calculate_pay()' function: %s" % calculate_pay.__annotations__)
    print("For 'print_pay_results()' function: %s" % print_pay_results.__annotations__)
    print("For 'print_annotations()' function: %s" % print_annotations.__annotations__)
    print("************************************************************************")


if __name__ == "__main__":
    worked_hours, hourly_rate = get_input_from_user()
    total_pay = calculate_pay(worked_hours, hourly_rate)
    print_pay_results(worked_hours, hourly_rate, total_pay)
    print_annotations()
