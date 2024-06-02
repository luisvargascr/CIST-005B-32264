"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 05/18/2024

File Name: main.py
Description: main
This file contains class on the MySocialNetwork class
and runs the program.
"""


from mysocialnetwork import MySocialNetwork

if __name__ == "__main__":
    """ Entry point to the application. """
    social_network_name = input("\nEnter the social network name (hit enter for default 'Facebook'): ")
    if social_network_name == "":
        social_network_name = "Facebook"
    network = MySocialNetwork(social_network_name)
    network.run()

"""
***************************** SAMPLE OUTPUT BELOW ******************************
/Users/luis/Documents/Classes/Programming/Python/CIST-005B-32264/ExtraCredit/pythonProject/.venv/bin/python /Users/luis/Documents/Classes/Programming/Python/CIST-005B-32264/Homework/pythonProject17/main.py 

Enter the social network name (hit enter for default 'Facebook'): 
================================================================================
                              Welcome to Facebook!                              
--------------------------------------------------------------------------------
Option: Description:   
--------------------------------------------------------------------------------
0       Show this menu.
1       Add a profile. 
2       Add friends.   
3       Read the information of an existing profile.
4       Update a profile.
5       Update the friend's list.
6       Delete a profile.
7       Delete a friend of a profile.
8       Exit           
================================================================================

Please enter your option: 1
*** Adding Profile ***
Enter Name: Luis Vargas
Enter E-Mail: lvargasc@mywvm.wvm.edu
Enter Phone Number: (408) 480-6090
You've created a profile.

Please enter your option: 1
*** Adding Profile ***
Enter Name: Joe Doe
Enter E-Mail: joedoe@mywvm.wvm.edy
Enter Phone Number: (669) 480-9262
You've created a profile.

Please enter your option: 4
*** Updating Existing Profile ***
Enter Name: Joe doe
Profile for Joe doe does NOT exist. Please try with a different name.

Please enter your option: 4
*** Updating Existing Profile ***
Enter Name: Joe Doe
Provide information for Joe Doe to update.
Enter Updated Name: Joe Doe
Enter Updated E-Mail: joedoe@mywvm.wvm.edu
Enter Updated Phone Number: (669) 480-9262

Please enter your option: 1
*** Adding Profile ***
Enter Name: Sarah O'connor
Enter E-Mail: sarahoconnor@mywvm.wvm.edu
Enter Phone Number: (501) 890-9089
You've created a profile.

Please enter your option: 1
*** Adding Profile ***
Enter Name: Douglas Kyles
Enter E-Mail: dougkyles@mywvm.wvm.edu
Enter Phone Number: (958) 879-6355
You've created a profile.

Please enter your option: 2
*** Adding Friend's to an Existing Profile ***
Enter Profile Name:  ('q' to quit): Luis Vargas
Enter Friend's Name:  ('q' to quit): Sarah O'connor
Luis Vargas and Sarah O'connor are now friends!

Please enter your option: 2
*** Adding Friend's to an Existing Profile ***
Enter Profile Name:  ('q' to quit): Luis vargas
No profile by that name was found. Please try again.
Enter Profile Name:  ('q' to quit): Luis Vargas
Enter Friend's Name:  ('q' to quit): Joe Doe
Luis Vargas and Joe Doe are now friends!

Please enter your option: 2
*** Adding Friend's to an Existing Profile ***
Enter Profile Name:  ('q' to quit): Sarah O'connor
Enter Friend's Name:  ('q' to quit): Douglas Kyles
Sarah O'connor and Douglas Kyles are now friends!

Please enter your option: 2
*** Adding Friend's to an Existing Profile ***
Enter Profile Name:  ('q' to quit): Douglas Kyles
Enter Friend's Name:  ('q' to quit): Felipe Hurtado
No profile by that name was found. Please try again.
Enter Friend's Name:  ('q' to quit): Joe Doe
Douglas Kyles and Joe Doe are now friends!

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis Vargas
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Luis Vargas.
Email: lvargasc@mywvm.wvm.edu.
Phone: (408) 480-6090.
Luis Vargas's friends are: ["Sarah O'connor", 'Joe Doe'].

Please enter your option: 4
*** Updating Existing Profile ***
Enter Name: Luis Vargas
Provide information for Luis Vargas to update.
Enter Updated Name: Luis A. Vargas
Enter Updated E-Mail: lvargasc@mywvm.wvm.edu
Enter Updated Phone Number: (408) 820-3347

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis Vargas
Profile for Luis Vargas does NOT exist. Please try with a different name.

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis A. Vargas
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Luis A. Vargas.
Email: lvargasc@mywvm.wvm.edu.
Phone: (408) 820-3347.
Luis A. Vargas's friends are: ["Sarah O'connor", 'Joe Doe'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Joe Doe
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Joe Doe.
Email: joedoe@mywvm.wvm.edu.
Phone: (669) 480-9262.
Joe Doe's friends are: ['Douglas Kyles', 'Luis A. Vargas'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Sarah O'connor
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Sarah O'connor.
Email: sarahoconnor@mywvm.wvm.edu.
Phone: (501) 890-9089.
Sarah O'connor's friends are: ['Douglas Kyles', 'Luis A. Vargas'].

Please enter your option: 5
*** Updating Friend's List for a Profile ***
Enter Name: Sarah O'connor
Sarah O'connor's friends are: ['Douglas Kyles', 'Luis A. Vargas'].
Enter 1 to add a friend or 2 to remove a friend: 
Enter option: 1
Enter Friend's Name:  ('q' to quit): Joe Doe
Sarah O'connor and Joe Doe are now friends!

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Sarah O'connor
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Sarah O'connor.
Email: sarahoconnor@mywvm.wvm.edu.
Phone: (501) 890-9089.
Sarah O'connor's friends are: ['Douglas Kyles', 'Luis A. Vargas', 'Joe Doe'].

Please enter your option: 5
*** Updating Friend's List for a Profile ***
Enter Name: Sarah O'connor
Sarah O'connor's friends are: ['Douglas Kyles', 'Luis A. Vargas', 'Joe Doe'].
Enter 1 to add a friend or 2 to remove a friend: 
Enter option: 2
Enter Friend's Name to remove: Luis A. Vargas
The friendship between Sarah O'connor and Luis A. Vargas was removed!

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Sarah O'connor
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Sarah O'connor.
Email: sarahoconnor@mywvm.wvm.edu.
Phone: (501) 890-9089.
Sarah O'connor's friends are: ['Douglas Kyles', 'Joe Doe'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis A. Vargas
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Luis A. Vargas.
Email: lvargasc@mywvm.wvm.edu.
Phone: (408) 820-3347.
Luis A. Vargas's friends are: ['Joe Doe'].

Please enter your option: 6
*** Deleting a Profile ***
Enter Name: Luis A. Vargas
Profile for Luis A. Vargas was deleted.

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis A. Vargas
Profile for Luis A. Vargas does NOT exist. Please try with a different name.

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Luis Vargas
Profile for Luis Vargas does NOT exist. Please try with a different name.

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Sarah O'connor
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Sarah O'connor.
Email: sarahoconnor@mywvm.wvm.edu.
Phone: (501) 890-9089.
Sarah O'connor's friends are: ['Douglas Kyles', 'Joe Doe'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Joe Doe
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Joe Doe.
Email: joedoe@mywvm.wvm.edu.
Phone: (669) 480-9262.
Joe Doe's friends are: ['Douglas Kyles', "Sarah O'connor"].

Please enter your option: 7
*** Deleting a Friend of a Profile ***
Enter Name: Sarah O'connor
Sarah O'connor's friends are: ['Douglas Kyles', 'Joe Doe'].
Enter Friend's Name to remove: Joe Doe
The friendship between Sarah O'connor and Joe Doe was removed!

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Sarah O'connor
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Sarah O'connor.
Email: sarahoconnor@mywvm.wvm.edu.
Phone: (501) 890-9089.
Sarah O'connor's friends are: ['Douglas Kyles'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Joe Doe
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Joe Doe.
Email: joedoe@mywvm.wvm.edu.
Phone: (669) 480-9262.
Joe Doe's friends are: ['Douglas Kyles'].

Please enter your option: 3
*** Reading the Information of an Existing Profile ***
Enter Name: Douglas Kyles
--------------------------------------------------------------------------------
Profile Information:
--------------------------------------------------------------------------------
Name: Douglas Kyles.
Email: dougkyles@mywvm.wvm.edu.
Phone: (958) 879-6355.
Douglas Kyles's friends are: ["Sarah O'connor", 'Joe Doe'].

Please enter your option: 8
Thank you for using Facebook!!!
================================================================================

Process finished with exit code 0

"""