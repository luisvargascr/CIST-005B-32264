"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/08/2024

Description: This program solves Chapter 2 Exercise 3:
1) Create a dictionary of your friends that you found in 2017 and 2018.
So, the keys are '2017' and '2018.
For example: friend_dict = {2017: ["Joe", "Lily"] , 2018: ["Bob", "Tom"]}
2) Print the friend's name
3) Ask the user to enter a name of their friends.
Then show the friend you found in 2017 or 2018.
4) Ask the user to add a new friend name to the 2017 or 2018 lists
(You need also to ask the user what year they want to add the friend name).
5) Then add the entered friend name to the dictionary(2017 or 2018  value)
Print the friends' dictionary on the screen.
"""


class Friendship:
    """
    This class implements essential methods to look up
    friends in either years 2017 or 2018, add a friend
    to the key of a dictionary
    representing the specific year, and print the
    contents of the dictionary.
    """

    def __init__(self):
        self.friend_dict = {2017: ["Joe", "Lily"], 2018: ["Bob", "Tom"]}

    def get_list_of_friends(self) -> None:
        """
        This method gets the two lists of friends, those for 2017 and 2018,
        from the dictionary and concatenates both and then prints
        them producing one output.
        :return: None
        """
        friends = []
        for key, value in self.friend_dict.items():
            friends += self.friend_dict[key]
        print(friends)

    def check_for_friend(self) -> None:
        """
        This method prompts the user to enter a friend's name
        and it will check if that name is present in either the
        2017 or 2018 list. If it does, it indicates on which
        list for the corresponding key in the dictionary
        the friend was found at. Otherwise, it will indicate
        that the name was not found.
        :return: None
        """

        friendName = input("Enter friend's name to search for: ").strip()
        foundFriendInAnyList = False

        for key, value in self.friend_dict.items():
            if friendName in self.friend_dict[key]:
                foundFriendInAnyList = True
                print("Your friend '%s' was found in the %s list" % (friendName, key))

        if not foundFriendInAnyList:
            print("You don't have any friend with this name '%s' in your friends' list." % friendName)

    def add_friend_to_specific_year_list(self) -> None:
        """
        This method prompts for a friend name and asks for which
        key in the dictionary, the user wants to add that
        new friend: the list for 2017 or the list for 2018.
        After that, it prints all friends from both years, 2017 and 2018.
        :return: None
        """
        friendName = input("Enter friend name: ").strip()

        try:
            year = int(input("Enter the year to add your friend (2017 or 2018): ").strip())
            if year == 2017 or year == 2018:
                self.friend_dict[year].append(friendName)
            else:
                print("Invalid input. Only 2017 and 2018 are valid years.")

        except ValueError:
            print("Invalid input. Only 2017 and 2018 are valid years.")

        for key, value in self.friend_dict.items():
            print("Friends' List of %s: %s" % (key, self.friend_dict[key]))


def process_friend_info():
    friend = Friendship()
    friend.get_list_of_friends()
    friend.check_for_friend()
    friend.add_friend_to_specific_year_list()


if __name__ == '__main__':
    process_friend_info()

"""
Example Output # 1:
--------------------

['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Lily
Your friend 'Lily' was found in the 2017 list
Enter friend name: Mike
Enter the year to add your friend (2017 or 2018): 2020
Invalid input. Only 2017 and 2018 are valid years.
Friends' List of 2017: ['Joe', 'Lily']
Friends' List of 2018: ['Bob', 'Tom']

Example Output # 2:
-------------------
['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Tom
Your friend 'Tom' was found in the 2018 list
Enter friend name: July
Enter the year to add your friend (2017 or 2018): 2018
Friends' List of 2017: ['Joe', 'Lily']
Friends' List of 2018: ['Bob', 'Tom', 'July']

Example Output # 3:
-------------------
['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Joe
Your friend 'Joe' was found in the 2017 list
Enter friend name: Tony
Enter the year to add your friend (2017 or 2018): 2017
Friends' List of 2017: ['Joe', 'Lily', 'Tony']
Friends' List of 2018: ['Bob', 'Tom']

Example Output # 4:
-------------------
['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Tom
Your friend 'Tom' was found in the 2018 list
Enter friend name: John
Enter the year to add your friend (2017 or 2018): trsf
Invalid input. Only 2017 and 2018 are valid years.
Friends' List of 2017: ['Joe', 'Lily']
Friends' List of 2018: ['Bob', 'Tom']

"""
