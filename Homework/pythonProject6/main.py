"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/07/2024

Description: This program solves Chapter 2 Exercise 2:
1) Create two lists of your friends that you found in 2017 and 2018. For example:
friends_2017 = ["Joe", "Lily"]
friends_2018 = ["Bob", "Tom"]
2) Concatenate the two lists and then show (print) them to the user.
3) Ask the user to enter a name of a friend.
Then show that you found the friend in 2017 or 2018, or they don't have any friend with this
name in their friends' list.
4) Ask the user to enter a new friend name to be added to the 2017 or 2018 lists
(Also, you need to ask the user what year they want to add the friend name).
5) Then append the entered friend name to the related list (2017 or 2018 friend lists)
6) Print the 2017 friends list and also the 2018 friends list on the screen.

For this exercise, you don't need to check the user inputs. Also, you don't need to use loops.
"""


class Friendship:
    """
    This class implements essential methods to look up
    friends in either years 2017 or 2018, add a friend
    to either list, and print the contents of these lists.
    """
    def __init__(self):
        self.friends_2017 = ["Joe", "Lily"]
        self.friends_2018 = ["Bob", "Tom"]

    def get_list_of_friends(self) -> None:
        """
        This method gets the two lists of friends, those for 2017 and 2018,
        and concatenates both and then prints them producing one output.
        :return: None
        """
        all_friends = self.friends_2017 + self.friends_2018
        print(all_friends)

    def check_for_friend(self) -> None:
        """
        This method prompts the user to enter a friend's name
        and it will check if that name is present in either the
        2017 or 2018 list. If it does, it indicates on which
        list the friend was found. Otherwise, it will indicate
        that the name was not found.
        :return: None
        """

        friendName = input("Enter friend's name to search for: ").strip()
        foundFriendInAnyList = False

        if friendName in self.friends_2017:
            print("Your friend '%s' was found in the list of friends of 2017." % friendName)
            foundFriendInAnyList = True
        if friendName in self.friends_2018:
            print("Your friend '%s' was found in the list of friends of 2018." % friendName)
            foundFriendInAnyList = True

        if not foundFriendInAnyList:
            print("You don't have any friend with this name '%s' in your friends' list." % friendName)

    def add_friend_to_specific_year_list(self) -> None:
        """
        This method prompts for a friend name and asks on
        which list, the user wants to add that new friend: 2017 or 2018.
        After that, it prints both lists of friends.
        :return: None
        """
        friendName = input("Enter friend name: ").strip()
        year = int(input("Enter the year to add your friend (2017 or 2018): ").strip())
        if year == 2017:
            self.friends_2017.append(friendName)
        elif year == 2018:
            self.friends_2018.append(friendName)
        else:
            print("Invalid input. Only 2017 and 2018 are valid years.")

        print("Friends' List of 2017: %s" % self.friends_2017)
        print("Friends' List of 2018: %s" % self.friends_2018)


if __name__ == '__main__':
    friend = Friendship()
    friend.get_list_of_friends()
    friend.check_for_friend()
    friend.add_friend_to_specific_year_list()

"""
Example Output # 1:
--------------------

['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Joe
Your friend 'Joe' was found in the list of friends of 2017.
Enter friend name: Mike
Enter the year to add your friend (2017 or 2018): 2017
Friends' List of 2017: ['Joe', 'Lily', 'Mike']
Friends' List of 2018: ['Bob', 'Tom']

Example Output # 2:
-------------------
['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Bob
Your friend 'Bob' was found in the list of friends of 2018.
Enter friend name: Jake
Enter the year to add your friend (2017 or 2018): 2018
Friends' List of 2017: ['Joe', 'Lily']
Friends' List of 2018: ['Bob', 'Tom', 'Jake']

Example Output # 3:
-------------------
['Joe', 'Lily', 'Bob', 'Tom']
Enter friend's name to search for: Lucas
You don't have any friend with this name 'Lucas' in your friends' list.
Enter friend name: Sandy
Enter the year to add your friend (2017 or 2018): 2020
Invalid input. Only 2017 and 2018 are valid years.
Friends' List of 2017: ['Joe', 'Lily']
Friends' List of 2018: ['Bob', 'Tom']

"""
