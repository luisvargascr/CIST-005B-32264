"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/18/2024

File Name: mysocialnetwork.py
Description: MySocialNetwork
This file contains the class MySocialNetwork which will be used to
represent a social network.

Exercise Description: The popular social network Facebook TM or Instagram was founded
by Mark Zuckerberg and his classmates at Harvard University in 2004. At the time,
he was a sophomore studying computer science.

Design and implement an application that maintains the data for a simple social network.
Each person in the network should have a profile that contains the person’s name.
Your application should allow a user to join the network, leave the network,
create a profile, modify the profile, search for other profiles, and add and remove friends.

"""

from graph import LinkedDirectedGraph
from myprofile import MyProfile


class MySocialNetwork(object):

    def __init__(self, social_network: str = "Your Social Network") -> None:
        """ Constructor for the class. """
        self.social_network_name = social_network
        self.options = {0: "Show this menu.",
                        1: "Add a profile.",
                        2: "Add friends.",
                        3: "Read the information of an existing profile.",
                        4: "Update a profile.",
                        5: "Update the friend's list.",
                        6: "Delete a profile.",
                        7: "Delete a friend of a profile."}
        self.exit_option = len(self.options.keys())
        self.my_network = LinkedDirectedGraph()
        self.current_profile = None

    def welcome_screen(self) -> None:
        """ Prints the welcome message at the beginning of the program. """
        print(("Welcome to %s!" % self.social_network_name).center(80))

    def show_main_options(self, show_header: bool = True) -> None:
        """ Shows the main menu to the customer on the screen. """
        if show_header:
            print("================================================================================")
            self.welcome_screen()
        print("--------------------------------------------------------------------------------")
        print("%-5s %-15s" % ("Option:", "Description:"))
        print("--------------------------------------------------------------------------------")
        for item_number, value in self.options.items():
            print("%-7d %-15s" % (item_number, value))
        print("%-7d %-15s" % (self.exit_option, "Exit"))
        if show_header:
            print("================================================================================")

    def run(self) -> None:
        """ Runs the whole program. """
        self.request_option()

    def request_option(self) -> None:
        """ Method that asks user what option from the main menu he/she wishes to use at any given time. """
        keep_asking_for_input = True
        self.show_main_options()

        while keep_asking_for_input:
            selection = self.__ask_option()
            if selection == self.exit_option:
                print("Thank you for using %s!!!" % self.social_network_name)
                print("================================================================================")
                keep_asking_for_input = False
            else:
                if selection == 0:
                    self.show_main_options(False)
                elif selection == 1:
                    self.add_profile()
                elif selection == 2:
                    self.add_friends_to_profile()
                elif selection == 3:
                    self.read_profile()
                elif selection == 4:
                    self.update_profile()
                elif selection == 5:
                    self.update_friends_list()
                elif selection == 6:
                    self.delete_profile()
                elif selection == 7:
                    self.delete_friend_of_profile()

    def __ask_option(self) -> int:
        """ Method that asks the customer to enter the option from the options available.
           It returns an integer representation of the menu option selected by the user. """
        is_option_valid = True
        selected_option = 0
        while is_option_valid:
            try:
                selected_option = int(input("\nPlease enter your option: ").strip())
                if selected_option == self.exit_option:
                    is_option_valid = False
                else:
                    is_option_valid = self.is_option_invalid(selected_option)

            except ValueError:
                print("\n*** Invalid option. Please enter 1-4 with option 5 to exit. ***\n")
                self.show_main_options(False)

        return selected_option

    def is_option_invalid(self, option: int) -> bool:
        """ Method that checks the validity of the menu option selected by the customer.
            If the option is valid, it returns True. Otherwise, it returns False. """
        if option not in self.options:
            print("\n*** Invalid option. Please enter 1-4 with option 5 to exit. ***\n")
            self.show_main_options(False)
            return True
        else:
            return False

    def add_profile(self) -> None:
        """ Method that adds a new profile. """
        print("*** Adding Profile ***")
        new_profile = MyProfile()
        name_new_profile = input("Enter Name: ")
        while name_new_profile == "":
            print("Name cannot be left blank. Please enter a valid name.")
            name_new_profile = input("Enter Name: ")
        new_profile.set_name(name_new_profile)
        new_profile.set_email(input("Enter E-Mail: "))
        new_profile.set_phone_number(input("Enter Phone Number: "))
        was_profile_found = self.my_network.containsVertex(new_profile.get_name())
        if not was_profile_found:
            self.my_network.add(new_profile)
            self.current_profile = new_profile
            print("You've created a profile.")
        else:
            print("Profile already exists!")

    def search_for_profile(self, message: str) -> MyProfile | None:
        """ Method that searches for a profile. If it finds it, it returns the profile object. Otherwise,
            returns None. """
        was_profile_found = False
        user_input = ""
        while not was_profile_found:
            user_input = input(message + " ('q' to quit): ")
            if user_input == "q":
                return None
            else:
                was_profile_found = self.my_network.containsVertex(user_input)
            if not was_profile_found:
                print("No profile by that name was found. Please try again.")
        return self.my_network.getVertexByName(user_input).profile

    def __is_network_empty(self) -> bool:
        """ Method that checks whether the social network is empty or not. If empty,
            it returns True. Otherwise, it returns False. """
        if self.my_network.sizeVertices() <= 0:
            print("You must add a profile before running this operation.")
            return True
        else:
            return False

    def add_friends_to_profile(self, profile_name: MyProfile = None) -> None:
        """ Method that adds friends (existing profiles are required) to an existing profile. """
        if self.__is_network_empty():
            return
        if not profile_name:
            print("*** Adding Friend's to an Existing Profile ***")
            profile_name = self.search_for_profile("Enter Profile Name: ")
        if profile_name:
            new_friend_name = self.search_for_profile("Enter Friend's Name: ")
            if new_friend_name:
                self.my_network.addEdge(profile_name, new_friend_name, 1)
                self.my_network.addEdge(new_friend_name, profile_name, 1)
                print("%s and %s are now friends!" % (profile_name.get_name(), new_friend_name.get_name()))

    def read_profile(self) -> None:
        """ Method that reads a specific profile from the social network. """
        if self.__is_network_empty():
            return
        print("*** Reading the Information of an Existing Profile ***")
        profile_name = input("Enter Name: ")
        profile_obj = self.my_network.getVertexByName(profile_name)
        if not profile_obj:
            print("Profile for %s does NOT exist. Please try with a different name." % profile_name)
        else:
            print("--------------------------------------------------------------------------------")
            print("Profile Information:")
            print("--------------------------------------------------------------------------------")
            print("Name: %s." % profile_obj.profile.get_name())
            print("Email: %s." % profile_obj.profile.get_email())
            print("Phone: %s." % profile_obj.profile.get_phone_number())
            friends_list = self.my_network.getIncidentEdges(profile_obj.profile)
            if len(friends_list) > 0:
                print("%s's friends are: %s." % (profile_name, str(friends_list)))
            else:
                print("%s does not have friends yet." % profile_name)

    def update_profile(self, profile_name: str = "") -> None:
        """ Method that updates an existing profile. """
        if self.__is_network_empty():
            return
        print("*** Updating Existing Profile ***")
        if not profile_name:
            profile_name = input("Enter Name: ")
        profile_obj = self.my_network.getVertexByName(profile_name)
        if not profile_obj:
            print("Profile for %s does NOT exist. Please try with a different name." % profile_name)
        else:
            print("Provide information for %s to update." % profile_obj.profile.get_name())
            updated_profile = MyProfile()
            updated_profile.set_name(input("Enter Updated Name: "))
            updated_profile.set_email(input("Enter Updated E-Mail: "))
            updated_profile.set_phone_number(input("Enter Updated Phone Number: "))
            self.my_network.updateVertex(profile_obj.profile, updated_profile)

    def update_friends_list(self) -> None:
        """ Method that updates the list of friends for an existing profile. """
        if self.__is_network_empty():
            return
        print("*** Updating Friend's List for a Profile ***")
        profile_name = input("Enter Name: ")
        profile_obj = self.my_network.getVertexByName(profile_name)
        if not profile_obj:
            print("Profile for %s does NOT exist. Please try with a different name." % profile_name)
        else:
            friends_list = self.my_network.getIncidentEdges(profile_obj.profile)
            if len(friends_list) > 0:
                print("%s's friends are: %s." % (profile_name, str(friends_list)))

                is_invalid = True
                option_to_update_list = 0

                while is_invalid:
                    print("Enter 1 to add a friend or 2 to remove a friend: ")
                    try:
                        option_to_update_list = int(input("Enter option: ").strip())
                        if option_to_update_list == 1 or option_to_update_list == 2:
                            is_invalid = False
                        else:
                            print("Invalid option, please enter 1 or 2.")
                    except ValueError:
                        continue

                if option_to_update_list == 1:
                    self.add_friends_to_profile(profile_obj.profile)
                else:
                    friend_to_remove = input("Enter Friend's Name to remove: ").strip()
                    friend_profile = self.my_network.getVertexByName(friend_to_remove)
                    if not friend_profile:
                        print("A friend by the name %s does not exist!" % friend_to_remove)
                    else:
                        self.my_network.removeEdgeByNames(profile_obj.profile.get_name(), friend_to_remove)
                        self.my_network.removeEdgeByNames(friend_to_remove, profile_obj.profile.get_name())
                        print("The friendship between %s and %s was removed!" % (profile_name, friend_to_remove))
            else:
                print("%s does not have any friends yet. You will now need to add friends. " % profile_name)
                self.add_friends_to_profile(profile_obj.profile)

    def delete_profile(self, profile: MyProfile = None) -> None:
        """ Method that deletes an existing profile. """
        if self.__is_network_empty():
            return
        print("*** Deleting a Profile ***")
        if not profile:
            profile_name = input("Enter Name: ")
            profile_detail = self.my_network.getVertexByName(profile_name)
            profile = profile_detail.profile if profile_detail else None

        if profile:
            self.my_network.removeVertex(profile)
            print("Profile for %s was deleted." % profile.get_name())
        else:
            print("Profile does not exist. No profile was deleted.")

    def delete_friend_of_profile(self, ):
        """ Method that deletes a friend from an existing profile. """
        if self.__is_network_empty():
            return
        print("*** Deleting a Friend of a Profile ***")
        profile_name = input("Enter Name: ")
        profile_obj = self.my_network.getVertexByName(profile_name)
        if not profile_obj:
            print("Profile for %s does NOT exist. Please try with a different name." % profile_name)
        else:
            friends_list = self.my_network.getIncidentEdges(profile_obj.profile)
            if len(friends_list) > 0:
                print("%s's friends are: %s." % (profile_name, str(friends_list)))
                friend_to_remove = input("Enter Friend's Name to remove: ").strip()
                friend_profile = self.my_network.getVertexByName(friend_to_remove)
                if not friend_profile:
                    print("A friend by the name %s does not exist!" % friend_to_remove)
                else:
                    self.my_network.removeEdgeByNames(profile_obj.profile.get_name(), friend_to_remove)
                    self.my_network.removeEdgeByNames(friend_to_remove, profile_obj.profile.get_name())
                    print("The friendship between %s and %s was removed!" % (profile_name, friend_to_remove))
            else:
                print("%s does not have any friends yet. " % profile_name)
