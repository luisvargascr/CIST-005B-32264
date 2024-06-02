"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: main
This file is used to run the Queue & Stack - Exercise - Palindrome
Consider this the entry point to the application.
"""

from palindrome import Palindrome


def print_result_palindrome_check(sentence: str) -> None:
    """Prints if a sentence is a palindrome or not. """
    palindrome = Palindrome()
    result = palindrome.is_palindrome(sentence)
    if result:
        print("The sentence '%s' is a palindrome." % sentence)
    else:
        print("The sentence '%s' is NOT a palindrome." % sentence)


if __name__ == "__main__":
    """Starting point of execution. """
    print_result_palindrome_check("Mr Owl ate my metal worm")
    print_result_palindrome_check("Madam")
    print_result_palindrome_check("Bugatti")
    print_result_palindrome_check("Todd")
