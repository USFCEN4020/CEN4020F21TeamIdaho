import string
import os

##### Displays
success_story = """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!
                                                                                - Gelo Pikalov"""

main_menu = """--------------- Login Page ---------------
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
"""

important_links_menu = """
Please choose one to learn more about:

1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Coyright Policy
8. Brand Policy
9. Languages
10. Return to the main menu
"""

useful_links_menu = """
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
"""

general_menu = """
1. Help Center
2. About
3. Press
4. Blog
5. Careers
6. Developers
7. Return
"""

logged_in_menu = """
1. Search for a Job / Internship
2. Find Someone That You May Know
3. Learn a New Skill
4. InCollege Important Links
5. Useful Links
6. Create Your User Profile
7. Edit Your User Profile
8. Create a Job
9. Edit a Job
10. Create Education
11. Edit Education
12. Display a User Profile
13. Exit
"""

skills_menu = """
1. Communication Skills
2. Management Skills
3. Business Skills
4. Analytical Skills
5. Information Technology (IT) Skills
6. I Want to Return to the Menu
"""

guest_controls_menu = """
1. InCollege Email
2. SMS
3. Targeted Advertising
4. None, Return to previous menu
"""

edit_profile_menu = """
1. Title
2. Major
3. University
4. About
5. Go Back
"""

edit_job_menu = """
1. Title
2. Employer
3. Date Started
4. Date Ended
5. Location
6. Description
7. Go Back
"""

edit_education_menu = """
1. School Name
2. Degree
3. Years Attended
4. Go Back
"""

def login_menu():
    print(main_menu)
    choice = integer_in_range("Choice: ", 1, 4, main_menu)
    return choice


# validation of password
def checkPasswordWorks(password):
    SpecialSymbol = ["$", "@", "#", "%", "!", "^", "&", "*"]
    if len(password) < 8 or len(password) > 12:
        print("Password Must be 8 - 12 Characters Long \n")
        return False
    elif not any(char.isdigit() for char in password):
        print("Make Sure Your Password has a Digit in it \n")
        return False
    elif not any(char.isupper() for char in password):
        print("Make Sure that the Password has a Capital Letter in it \n")
        return False
    elif not any(char in SpecialSymbol for char in password):
        print("Make Sure that the Password has a Special Letter in it \n")
        return False
    else:
        return True


# validation of password
def importantLinks(choice):
    if choice == 1:
        print(
            "\nThis faux application for Walmart LinkedIn is protected by Copyright Laws. \nReproduction of this code without permission is prohibited you baka"
        )
    elif choice == 2:
        print(
            "\nWelcome to In College, the world's largest college student network with many users in many countries and territories worldwide"
        )
    elif choice == 3:
        print(
            "\nThe Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. \nIt defines three levels of conformance: Level A, Level AA, and Level AAA. InCollege is fully conformant with WCAG 2.1 level AA. \nFully conformant means that the content fully conforms to the accessibility standard without any exceptions."
        )
    elif choice == 4:
        print(
            "\nThis User Agreement is effective upon acceptance for new users, and from September 28th, 2021 for existing user."
        )
    elif choice == 5:
        print(
            "\nWe take privacy very seriously. \nWe promise to not share your private information to any third-party. \nWe use maximum security to protect your information."
        )
        guestControls()
    elif choice == 6:
        print(
            "\nTeam Idaho may use cookies, web beacons, tracking pixels, and other tracking technologies whhen you use our software. \nThis helps to customize the application best suited for you."
        )
    elif choice == 7:
        print(
            "\nTeam Idaho respoects the intellectual property rights of others and expects the same for the users using this application."
        )
    elif choice == 8:
        print("\nWe change students' lives everyday. It's your turn now!")
    elif choice == 9:
        print("Choose a language, English or Spanish?\n")
        langChoice = integer_in_range(
            "Enter 1 for English and 2 for Spanish: ", 1, 2, "NULL"
        )
        if langChoice == 2:
            print("Language changed to Spanish")
        else:
            print("Language changed to English")


#### THESE DO NOT RETAIN THEIR INFO PER USER
def guestControls():
    print(guest_controls_menu)
    choice = integer_in_range("Choose which to toggle: ", 1, 4, guest_controls_menu)

    while choice != 4:
        if choice == 1:
            print("Emails have been toggled.")
        if choice == 2:
            print("SMS have been toggled.")
        if choice == 3:
            print("Targeted Ads have been toggled.")
        if choice == 4:
            return 0

        print(guest_controls_menu)
        choice = integer_in_range("Choose which to toggle: ", 1, 4, guest_controls_menu)


###########################################
##### Types of Inputs with validation #####
###########################################


def integer_in_range(prompt, low, high, menu):

    number = input(prompt)

    while (not number.isnumeric()) or (int(number) < low) or (int(number) > high):
        clear()
        print("\nPlease select a valid option.\n")

        if menu != "NULL":
            print(menu)

        number = input(prompt)

    return int(number)


##### Types of Inputs with validation
def integer(prompt):

    number = input(prompt)

    while not number.isnumeric():
        print("\nPlease select a valid option.\n")
        number = input(prompt)

    return int(number)


########## STRINGS

## This string input can have ANY characters EXCEPT spaces
def single_line_string(prompt):

    string_in = input(prompt)

    while " " in string_in:
        print("\nPlease type a valid response.\n")
        string_in = input(prompt)

    return string_in


## This string input can NOT have any numerical characters
def single_line_alphaString(prompt):

    string_in = input(prompt)

    while not string_in.isalpha():
        print("\nPlease type a valid response.\n")
        string_in = input(prompt)

    return string_in


def tryAgain():

    string_in = input("Would you like to try again? (Yes / No): ")
    acceptable = ["yes", "y", "no", "n"]

    while (not string_in.isalpha()) or (string_in.lower() not in acceptable):
        print("\nPlease type a valid response.\n")
        string_in = input("Would you like to try again? (Yes / No): ")

    if string_in.lower() == "yes" or string_in.lower() == "y":
        return True
    else:
        return False


## This string input CAN have any numerical characters
def single_line_alphaNumString(prompt):

    string_in = input(prompt)

    while not string_in.isalnum():
        print("\nPlease type a valid response.\n")
        string_in = input(prompt)

    return string_in


## This takes in any amount of lines - Any characters are valid
def mutli_line_string(prompt):

    string_in = input(prompt)
    string_in += "\n"
    temp = " "

    while not (temp == ""):
        temp = input("")
        string_in += temp + "\n"

    return string_in


# Clear Screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

