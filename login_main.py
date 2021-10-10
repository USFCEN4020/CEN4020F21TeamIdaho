import database
import logged_in
import ui

import re
import sqlite3

############ The Main Method will only handle the Main Menu
def main():

    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()

    ##### Main Menu
    ui.clear()
    print(ui.success_story)
    option = ui.login_menu()

    ##### Handle Main Menu Choice

    ## Login to Account
    if option == 1:
        database.listAllUsers()

        TryAgain = True
        while TryAgain == True:
            LoggedIn = database.login_credentials()
            if LoggedIn[0]:
                TryAgain = False
            else:
                TryAgain = ui.tryAgain()

        if LoggedIn[0]:
            print(ui.logged_in_menu)
            choice = ui.integer_in_range("Pick an Option: ", 1, 13, ui.logged_in_menu)
            while choice != 13:

                if choice == 1:
                    logged_in.jobBoard()
                    input("\nPress enter to return to menu...")

                elif choice == 2:
                    database.checkNameExists()

                elif choice == 3:
                    print(ui.skills_menu)
                    skills_choice = ui.integer_in_range(
                        "Pick an Option: ", 1, 6, ui.skills_menu
                    )

                    while skills_choice != 6:

                        logged_in.skills(skills_choice)

                        print(ui.skills_menu)
                        skills_choice = ui.integer_in_range(
                            "Pick an Option: ", 1, 6, ui.skills_menu
                        )

                elif choice == 4:
                    print(ui.important_links_menu)
                    option = ui.integer_in_range(
                        "Please choose an option to learn about: ",
                        1,
                        10,
                        ui.important_links_menu,
                    )
                    while option != 10:
                        ui.importantLinks(option)
                        print(ui.important_links_menu)
                        option = ui.integer_in_range(
                            "Please choose an option to learn about: ",
                            1,
                            10,
                            ui.important_links_menu,
                        )

                elif choice == 5:
                    logged_in.usefulLinks()

                elif choice == 6:
                    database.createUserProfile(LoggedIn[1])

                elif choice == 7:
                    database.editUserProfile(LoggedIn[1])

                elif choice == 8:
                    database.createJob(LoggedIn[1])

                elif choice == 9:
                    database.editJob(LoggedIn[1])

                elif choice == 10:
                    database.createEducation(LoggedIn[1])

                elif choice == 11:
                    database.editEducation(LoggedIn[1])

                elif choice == 12:
                    userRequested = ui.single_line_alphaString("Type the username of the user you want to see the profile for or \"exit\" to return: ")
                    while((not database.checkUsernameExists(userRequested)) and userRequested.lower() != "exit"):
                        print("That username isn't in the system. Try Again or type exit to leave.\n")
                        userRequested = ui.single_line_alphaString("Type the username of the user you want to see the profile for or \"exit\" to return: ")
                    
                    if userRequested.lower() != "exit":
                        database.displayUser(userRequested)

                print(ui.logged_in_menu)
                choice = ui.integer_in_range(
                    "Pick an Option: ", 1, 13, ui.logged_in_menu
                )

        print("Goodbye, Have a Nice Day !")
        raise SystemExit(0)

    ## Create an Account
    if option == 2:
        database.createAccount()
        main()

    if option == 3:
        print(ui.important_links_menu)
        option = ui.integer_in_range(
            "Please choose an option to learn about: ", 1, 10, ui.important_links_menu
        )
        if option != 10:
            ui.importantLinks(option)
        else:
            main()

    if option == 4:
        logged_in.usefulLinks()
        main()


if __name__ == "__main__":
    main()

