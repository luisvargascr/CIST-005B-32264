"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team: The Infinite Loop

Description: This script will do the following:
1) Ask the user to enter an email address.
2) Check that it is a valid email address => it should have "@"  and "."  {if '@' and '.' in user_input:}
3) Find the domain name of the email address and print it

Exercise 4
"""


def ask_email() -> str:
    is_email_invalid = True
    email_address = ""

    while is_email_invalid:
        email_address = input("Enter valid email: ")

        # Check if email provided contains at sign @ and at least one period.
        if email_address.find("@") > 0 and email_address.find(".") > 0:
            at_sign_index = email_address.rindex("@")
            last_dot_index = email_address.rindex(".")

            # Assumption: the email will be valid only if the last period is AFTER the at @ sign.
            is_email_invalid = False if at_sign_index < last_dot_index else True
        else:
            is_email_invalid = True

        if is_email_invalid:
            print("Invalid email. Please enter again.")

    return email_address


def find_domain(email: str) -> str:
    # Print the domain by using slice operator in string from position @ plus one until position of the last period.
    return email[email.index("@") + 1: email.rindex(".")]


if __name__ == '__main__':
    my_email_address = ask_email()
    print(find_domain(my_email_address))

"""
Sample Outputs:

Output 1:
---------
Enter valid email: luis.a.vargas@intel
Invalid email. Please enter again.
Enter valid email: luis.a.vargas@intel.com
intel

Output 2:
---------
Enter valid email: joe.doe@yahoo.com
yahoo

Output 3:
---------
Enter valid email: joey
Invalid email. Please enter again.
Enter valid email: joey@
Invalid email. Please enter again.
Enter valid email: joey.mac@
Invalid email. Please enter again.
Enter valid email: joey.mac@apple
Invalid email. Please enter again.
Enter valid email: joey.mac@apple.com
apple

"""