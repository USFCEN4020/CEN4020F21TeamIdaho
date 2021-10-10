import ui
import database


def jobBoard():
    print("############# Job Board #############")


def skills(choice):
    if choice == 1:
        print("Skill 1: Under Construction")
    elif choice == 2:
        print("Skill 2: Under Construction")
    elif choice == 3:
        print("Skill 3: Under Construction")
    elif choice == 4:
        print("Skill 4: Under Construction")
    elif choice == 5:
        print("Skill 5: Under Construction")


def importantLinks():
    print()


def usefulLinks():
    print(ui.useful_links_menu)
    option = ui.integer_in_range(
        "Please choose an option to learn about: ", 1, 5, ui.useful_links_menu
    )

    while not (option == 5):

        if option == 1:
            print(ui.general_menu)
            general_option = ui.integer_in_range(
                "Please choose an option to learn about: ", 1, 7, ui.general_menu
            )
            while not (general_option == 7):

                if general_option == 1:
                    print("We're here to help")
                elif general_option == 2:
                    print(
                        "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"
                    )
                elif general_option == 3:
                    print(
                        "In College Pressroom: Stay on top of the latest news, updates, and reports"
                    )
                elif general_option == 4:
                    print("Under construction")
                elif general_option == 5:
                    print("Under construction")
                elif general_option == 6:
                    print("Under construction")

                print(ui.general_menu)
                general_option = ui.integer_in_range(
                    "Please choose an option to learn about: ", 1, 7, ui.general_menu
                )

        elif option == 2:
            print("Under construction")
        elif option == 3:
            print("Under construction")
        elif option == 4:
            print("Under construction")

        print(ui.useful_links_menu)
        option = ui.integer_in_range(
            "Please choose an option to learn about: ", 1, 5, ui.useful_links_menu
        )

