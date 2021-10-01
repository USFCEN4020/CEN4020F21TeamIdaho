import Database
import sqlite3
import re

## this is the python file for the login page

# main page with 5 diffent options
#   -> these are the 5 accounts that have been created


def newAccount (username, password, first_name, last_name):

    #process to create a new account
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()  

    find_user = ("SELECT * FROM user WHERE username = ?")
    cursor.execute(find_user,[(username)])
    results = cursor.fetchall()
    

    cursor.execute("""
    INSERT INTO user (username,password, first_name, last_name) VALUES(?,?,?,?)""", (username,password,first_name,last_name))
    db.commit()
    

    print("You Have Registered", username)
    print()

def LoginAccount(username,password):
    #process to open a page
    #print("You Have Reached the Login Page")
    print()

    #makes a connection to the database
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()    
    # makes a query request to the database for username and password
    find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
    cursor.execute(find_user,[(username),(password)])

    #collects all the results
    results = cursor.fetchall()

    #if record exists 
    if results:
        for i in results:
            print("You have Logged In", i[1])
            print()
            break
    #once logged in, options presented to user
        while True:
            print("Pick an Option:")
            print("  1. Search for a job/internship\n"
                "  2. Find someone that you may know\n"
                "  3. Learn a new skill\n"
                "  4. InCollege Important Links\n"
                "  5. Useful Links")
            logOption = input("Choice: ")
            ilogOption = int(logOption)
            # search for a job/internship
            if ilogOption == 1:
                if ilogOption == 1:
                    print("\nWelcome to the job posting page\n")
                    print("""
                    Software Engineering Internship (SpaceX) -- Palo Alto, California
                    Minimum requirements
                    - Bachelor's degree in Computer Science/ Computer Engineering
                    - Experience in Jira
                    - Experience in Agile Environment
                    - Good experience in Java, C++, C
                    - Must have experience in Deep learning and Big data

                    Application Deadline 10/01/2021

                            Apply Now

""")
                again = input("Do You Want to Try Again? (yes/no): ").lower()

                if again == "no" or again == "n":
                    print("Goodbye")
                    exit()
                elif again == "yes" or again == "y":
                    main()
                else:   
                    print("Error with choice")
                    exit()

            # find someone that you may know
            elif ilogOption == 2:
                first = input("Enter First Name: ")
                last = input("Enter Last Name: ")
                # Check if user is in system
                find_someone = ("SELECT * FROM user WHERE first_name = ? AND last_name = ?")
                cursor.execute(find_someone,[(first),(last)])
                exist = cursor.fetchall()
                if exist:
                    for i in exist:
                        print("\nThey are a part of the InCollege System")
                        print()
                        break
                else:
                # not in system
                    print("\nThey are not yet a part of the InCollege system yet\n")

            # learn a new skill
            elif ilogOption == 3:
                print("Pick a Skill to Learn More About")
                print("1. Communication Skills\n"
                    "2. Management Skills\n"
                    "3. Business Skills\n"
                    "4. Analytical Skills\n"
                    "5. Information Technology (IT) Skills\n"
                    "6. I Want to Return to the Menu\n")
                skillOption = input("Choice: ")
                skillOption = int(skillOption)
                if skillOption == 1:
                    print("Under Construction")
                    break
                elif skillOption == 2:
                    print("Under Construction")
                    break
                elif skillOption == 3:
                    print("Under Construction")
                    break
                elif skillOption == 4:
                    print("Under Construction")
                    break
                elif skillOption == 5:
                    print("Under Construction")
                    break
                # option to not select skill, return to menu
                elif skillOption == 6:
                    print("Are You Sure You Want to Return?")
                    returnOption = input("Choice: ")
                    if returnOption.lower() in ['y', 'yes']:
                        print("")
                        continue
                    elif returnOption.lower() in ['n', 'no']:
                        break
                    elif skillOption > 6 or skillOption < 1:
                        print("Incorrect Option")
                        break                        
            # Implemented a fourth option for InCollege Links where it displays all the options indicated on Epic 3.
            elif ilogOption == 4:
                print("Please choice one to learn more about")
                print("1. Copyright Notice\n"
                      "2. About\n"
                      "3. Accessibility\n"
                      "4. User Agreement\n"
                      "5. Privacy Policy\n"
                      "6. Cookie Policy\n"
                      "7. Copyright Policy\n"
                      "8. Brand Policy\n"
                      "9. Languages\n")
                LinkOption = input("Please choose an option: ")
                impLinkOption = int(LinkOption)
                if impLinkOption == 1:
                    print("This faux application for Walmart LinkedIn is protected by Copyright Laws. Reproduction of this code without permission is prohibited you baka")
                    break
                elif impLinkOption == 2:
                    print("Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
                    break
                elif impLinkOption == 3:
                    print("The Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. It defines three levels of conformance: Level A, Level AA, and Level AAA. InCollege is fully conformant with WCAG 2.1 level AA. Fully conformant means that the content fully conforms to the accessibility standard without any exceptions.")
                    break
                elif impLinkOption == 4:
                    print("This User Agreement is effective upon acceptance for new users, and from September 28th, 2021 for existing user.")
                    break
                elif impLinkOption == 5:
                    print("We take privacy very seriously. We promise to not share your private information to any third-party. We use maximum security to protect your information.\n"
                    "You also have reached the Guest Controls, where you\n"
                            "You can choose which ones to turn off.\n"
                            "1. InCollege Email\n"
                            "2. SMS\n"
                            "3. Targeted Advertising\n"
                            "4. None of them, return back to menu\n")
                    # Using a boolean variable when it's False, it will go to another function (to be made later?) and actively turn off the features
                    onEmail, onSMS, onTargetAd = True
                    intChoice = input("Please input: ")
                    intChoice = int(intChoice)
                    if intChoice == 1: 
                        onEmail = False
                    elif intChoice == 2:
                        onSMS = False
                    elif intChoice == 3: 
                        onTargetAd = False
                    elif intChoice == 4:
                        print("Going back to main!")
                        main()
                    break
                elif impLinkOption == 6:
                    print("Team Idaho may use cookies, web beacons, tracking pixels, and other tracking technologies whhen you use our software. This helps to customize the application best suited for you.")
                    break
                elif impLinkOption == 7:
                    print("Team Idaho respoects the intellectual property rights of others and expects the same for the users using this application.")
                    break
                elif impLinkOption == 8: 
                    print("We change students' lives everyday. It's your turn now!")
                    break
                elif impLinkOption == 9:
                    #This will give the ability for user's to change the language of the app. 
                    print("Choose a language, English or Spanish?\n")
                    langChoice = input("Enter 1 for English and 2 for Spanish: ")
                    langChoice = int(langChoice)
                    if langChoice == 2:
                        print("Language changed to Spanish")
                    else:
                        print("Language changed to English")
            elif ilogOption == 5:
                # Useful links menu
                checker = 0
                while checker != 5:
                    print("Please choose one to learn more about")
                    print("1. General\n"
                          "2. Browse InCollege\n"
                          "3. Business Solutions\n"
                          "4. Directories\n"
                          "5. Return")
                    checker = input("Option: ")
                    checker = int(checker)
                    if checker == 1:
                        sub_ans = 0
                        while sub_ans!= 7:
                            print("1. Help Center\n"
                                  "2. About\n"
                                  "3. Press\n"
                                  "4. Blog\n"
                                  "5. Careers\n"
                                  "6. Developers\n"
                                  "7. Return\n")
                            sub_ans = input("Option: ")
                            sub_ans = int(sub_ans)
                            while sub_ans > 7 or sub_ans < 1:
                                sub_ans = input("ERROR. Option: ")
                                sub_ans = int(sub_ans)

                            if sub_ans == 1:
                                print("We're here to help")
                            if sub_ans == 2:
                                print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
                            if sub_ans == 3:
                                print("In College Pressroom: Stay on top of the latest news, updates, and reports")
                            if sub_ans == 4:
                                print("Under construction")
                            if sub_ans == 5:
                                print("Under construction")
                            if sub_ans == 6:
                                print("Under construction")

                    elif checker == 2:
                        print("Under construction")
                    elif checker == 3:
                        print("Under construction")
                    elif checker == 4:
                        print("Under construction")

            elif ilogOption > 5 or ilogOption < 1:
                print("Incorrect Option")
                break
    #if record does not exist
        else:
            print("Incorrect Username/Password, Please Try Again")
            again = input("Do You Want to Try Again? (yes/no): ").lower()

            if again == "no" or again == "n":
                print("Goodbye")
                exit()
            elif again == "yes" or again == "y":
                main()
            else:   
                print("Error with choice")

    print()
    raise SystemExit(0)

########################################

import re

def main():

    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()  
            
    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()
    
    # Success story
    print("\n----- Success Story -----")
    print(" 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.")
    print("                  Now I'm flipping patties and making more money than my friends!'")
    print("                                                                                - Gelo Pikalov")
    
    print("----- Login Page -----")
    print("Please Select One of the Following Options")

    # ask for choice
    print("""
1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
""")

    option = input ("Choice: ")
    # convert string to int
    newOption = int(option)

    print()


    ## these are the options that you make your choices with
    if newOption == 1:
        print("Existing Accounts:")
        number = 1
        for i in results:
            print(f'  {number}: {i[1]}')
            number = number + 1

        print()
        #login to account 
        print("- Enter Credentials to Login -")
        username = input("Enter Name:")
        password = input("Enter Password:")

        #validation of password 
        if len(password)<8:
            print("Password Must be 8 Characters Long\n")
            main()
            
        elif not any(char.isdigit() for char in password):
            print("Make Sure Your Password has a Digit in it.\n")
            main()
            
        elif not any(char.isupper() for char in password):
            print("Make Sure that the Password has a Capital Letter in it\n")
            main()
            
        else:
            print()
            #passing arguements to login function 
            LoginAccount(username,password)  

    elif newOption == 2:
        #checking if 6th attempt is made
        cursor.execute("SELECT COUNT(*) FROM user")
        accResults = cursor.fetchall()
        if len(accResults) >= 6:
            print("All Permitted Accounts Have Been Created, Please Log in if You Have an Account.")
        else:
            ## create a new account
            ## The main statements are commented out for testing the password only
            
            print("Enter Credentials to Login:")
            username = input("Enter Username:")
            

            find_user = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(find_user,[(username)])
            results = cursor.fetchall()

            for i in results:
                print("An Account of that username exists")
                choice = input("Try login again? (yes,no)")
                if choice == "yes":
                    main()
                elif choice == "no":
                    exit()
                else:
                    exit()
            else:
                password = input("Enter Account Password: ")
                #validation of password 
                SpecialSymbol = ['$', '@', '#', '%', '!', '^', '&', '*']

                if len(password)<8 or len(password)>12:
                    print("Password Must be 8 - 12 Characters Long \n")
                    main()
                elif not any(char.isdigit() for char in password):
                    print("Make Sure Your Password has a Digit in it \n")
                    main()
                elif not any(char.isupper() for char in password):
                    print("Make Sure that the Password has a Capital Letter in it \n")
                    main()
                elif not any(char in SpecialSymbol for char in password):
                    print("Make Sure that the Password has a Special Letter in it \n")
                    main()
                else:
                    # Get first and last name from user
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    print()
                    # Passing arguments to new account function.
                    newAccount(username,password,first_name,last_name)
                    main()
    #This adds the important links not only for Logged In users but guests visiting the site as well.
    elif newOption == 3:
        print("Please choose one to learn more about")
        print("1. Copyright Notice\n"
                      "2. About\n"
                      "3. Accessibility\n"
                      "4. User Agreement\n"
                      "5. Privacy Policy\n"
                      "6. Cookie Policy\n"
                      "7. Coyright Policy\n"
                      "8. Brand Policy\n"
                      "9. Return to the main menu\n")
        LinkOption = input("Option: ")
        impLinkOption = int(LinkOption)
        if impLinkOption == 1:
            print("This faux application for Walmart LinkedIn is protected by Copyright Laws. Reproduction of this code without permission is prohibited you baka")
        elif impLinkOption == 2:
            print("Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        elif impLinkOption == 3:
            print("The Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. It defines three levels of conformance: Level A, Level AA, and Level AAA. InCollege is fully conformant with WCAG 2.1 level AA. Fully conformant means that the content fully conforms to the accessibility standard without any exceptions.")
        elif impLinkOption == 4:
            print("This User Agreement is effective upon acceptance for new users, and from September 28th, 2021 for existing user.")
        elif impLinkOption == 5:
            print("We take privacy very seriously. We promise to not share your private information to any third-party. We use maximum security to protect your information.")
        elif impLinkOption == 6:
            print("Team Idaho may use cookies, web beacons, tracking pixels, and other tracking technologies whhen you use our software. This helps to customize the application best suited for you.")
        elif impLinkOption == 7:
            print("Team Idaho respoects the intellectual property rights of others and expects the same for the users using this application.")
        elif impLinkOption == 8: 
            print("We change students' lives everyday. It's your turn now!")
        elif impLinkOption == 9:
            main()
    elif newOption == 4:
            # Useful links menu
            checker = 0
            while checker!=5:
                print("Please choose one to learn more about")
                print("1. General\n"
                      "2. Browse InCollege\n"
                      "3. Business Solutions\n"
                      "4. Directories\n"
                      "5. Return")
                checker = input("Option: ")
                checker = int(checker)
                if checker == 1:
                    sub_ans = 0
                    while sub_ans!=8:
                        print("1. Sign Up\n"
                              "2. Help Center\n"
                              "3. About\n"
                              "4. Press\n"
                              "5. Blog\n"
                              "6. Careers\n"
                              "7. Developers\n"
                              "8. Return\n")
                        sub_ans= input("Option: ")
                        sub_ans = int(sub_ans)
                        while sub_ans > 9 or sub_ans < 1:
                            sub_ans = input("ERROR. Option: ")
                            sub_ans = int(sub_ans)
                        if sub_ans == 1:
                            # Copied from above. Rewrite in method to avoid mess
                            # checking if 6th attempt is made
                            cursor.execute("SELECT COUNT(*) FROM user")
                            accResults = cursor.fetchall()
                            if len(accResults) >= 6:
                                print("All Permitted Accounts Have Been Created, Please Log in if You Have an Account.")
                            else:
                                ## create a new account
                                ## The main statements are commented out for testing the password only

                                print("Enter Credentials to Login:")
                                username = input("Enter Username:")

                                find_user = ("SELECT * FROM user WHERE username = ?")
                                cursor.execute(find_user, [(username)])
                                results = cursor.fetchall()

                                for i in results:
                                    print("An Account of that username exists")
                                    choice = input("Try login again? (yes,no)")
                                    if choice == "yes":
                                        main()
                                    elif choice == "no":
                                        exit()
                                    else:
                                        exit()
                                else:
                                    password = input("Enter Account Password: ")
                                    # validation of password
                                    SpecialSymbol = ['$', '@', '#', '%', '!', '^', '&', '*']

                                    if len(password) < 8 or len(password) > 12:
                                        print("Password Must be 8 - 12 Characters Long \n")
                                        main()
                                    elif not any(char.isdigit() for char in password):
                                        print("Make Sure Your Password has a Digit in it \n")
                                        main()
                                    elif not any(char.isupper() for char in password):
                                        print("Make Sure that the Password has a Capital Letter in it \n")
                                        main()
                                    elif not any(char in SpecialSymbol for char in password):
                                        print("Make Sure that the Password has a Special Letter in it \n")
                                        main()
                                    else:
                                        # Get first and last name from user
                                        first_name = input("Enter first name: ")
                                        last_name = input("Enter last name: ")
                                        print()
                                        # Passing arguments to new account function.
                                        newAccount(username, password, first_name, last_name)
                                        main()
                        if sub_ans == 2:
                            print("We're here to help")
                        if sub_ans == 3:
                            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
                        if sub_ans == 4:
                            print("In College Pressroom: Stay on top of the latest news, updates, and reports")
                        if sub_ans == 5:
                            print("Under construction")
                        if sub_ans == 6:
                            print("Under construction")
                        if sub_ans == 7:
                            print("Under construction")

                elif checker == 2:
                    print("Under construction")
                elif checker == 3:
                     print("Under construction")
                elif checker == 4:
                    print("Under construction")
    elif newOption > 5 or newOption < 0:
        print("Incorrect Option ")
        main()
 
if __name__ == '__main__':
    main()
