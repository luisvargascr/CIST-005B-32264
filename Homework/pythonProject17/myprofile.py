"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/18/2024

File Name: profile.py
Description: Profile
This file contains the class Profile which will be used to
represent a single individual in a social network.
"""


class MyProfile(object):
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__phone_number = ""

    def set_name(self, profile_name: str) -> None:
        """ Sets the name of the profile. """
        self.__name = profile_name

    def get_name(self) -> str:
        """ Gets the name of the profile. """
        return self.__name

    def set_email(self, email_address: str) -> None:
        """ Sets the email of the profile. """
        self.__email = email_address

    def get_email(self) -> str:
        """ Gets the email of the profile. """
        return self.__email

    def set_phone_number(self, phone_num: str) -> None:
        """ Sets the phone number of the profile. """
        self.__phone_number = phone_num

    def get_phone_number(self) -> str:
        """ Gets the phone number of the profile. """
        return self.__phone_number
