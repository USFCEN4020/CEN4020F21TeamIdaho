import sqlite3

import re
import sqlite3

import ui
import Database

import time
import datetime


########################################################################################## Logged In Functions

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
    option = integer_in_range(
        "Please choose an option to learn about: ", 1, 5, ui.useful_links_menu
    )

    while not (option == 5):

        if option == 1:
            print(ui.general_menu)
            general_option = integer_in_range(
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
                general_option = integer_in_range(
                    "Please choose an option to learn about: ", 1, 7, ui.general_menu
                )

        elif option == 2:
            print("Under construction")
        elif option == 3:
            print("Under construction")
        elif option == 4:
            print("Under construction")

        print(ui.useful_links_menu)
        option = integer_in_range(
            "Please choose an option to learn about: ", 1, 5, ui.useful_links_menu
        )


#################################################################################################### Database Functions

def createAccount():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if there are 5 user accounts already
    cursor.execute("SELECT COUNT(*) FROM user")
    number = cursor.fetchall()

    if (len(number)) >= 11:
        print(
            "All Permitted Accounts Have Been Created, Please Log in if You Have an Account."
        )

    else:
        username = single_line_alphaString("Enter Username: ")
        while checkUsernameExists(username):
            print("\nAn Account of that username exists, Try Again.\n")
            username = single_line_alphaString("Enter Username:")

        password = single_line_string("Enter Account Password: ")
        while not checkPasswordWorks(password):
            password = single_line_string("Enter Account Password: ")

        firstName = single_line_alphaNumString("Enter First Name: ")
        lastName = single_line_alphaNumString("Enter Last Name: ")
        statusAcc = single_line_string("Enter Standard or Plus: ")

        cursor.execute(
            """
        INSERT INTO user (username, password, first_name, last_name, tier_name) VALUES(?,?,?,?,?)""",
            (username, password, firstName, lastName, statusAcc),
        )
        db.commit()

        print("You Have Registered", username)


def checkUsernameExists(Username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_user = "SELECT * FROM user WHERE username = ?"
    cursor.execute(find_user, [(Username)])
    results = cursor.fetchall()
    cursor.close()

    if len(results) > 0:
        return True
    else:
        return False


def checkNameExists(me):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    # Check if user is in system
    find_someone = "SELECT * FROM user WHERE first_name = ? AND last_name = ?"
    cursor.execute(find_someone, [(first), (last)])
    exist = cursor.fetchall()

    usernames = []
    for each in exist:
        usernames.append(each[1])

    if len(exist) > 0:
        print("Users with that name ", last, ": ")
        for user in exist:
            print("Username: ", user[1], ", Name: ", user[3], " ", user[4])

        if wantSendRequest() == True:
            requested = single_line_alphaNumString("Enter their username: ")
            if requested in usernames:
                friend_request(me, requested)
            else:
                print("That isn't their username.")
    else:
        print("They are not yet a part of the InCollege system yet")


def listByLastName(me):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    last = input("Enter Last Name: ")
    # Check if user is in system
    find_someone = "SELECT * FROM user WHERE last_name = ?"
    cursor.execute(find_someone, [(last)])
    exist = cursor.fetchall()

    usernames = []
    for each in exist:
        usernames.append(each[1])

    if len(exist) > 0:
        print("Users with the last name ", last, ": ")
        for user in exist:
            print("Username: ", user[1], ", Name: ", user[3], " ", user[4])

        if wantSendRequest() == True:
            requested = single_line_alphaNumString("Enter their username: ")
            if requested in usernames:
                friend_request(me, requested)
            else:
                print("That isn't one of the usernames.")

    else:
        print("There is nobody with that last name")


def listByUniversity(me):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    uni = input("Enter University: ").title()
    # Check if user is in system
    find_someone = "SELECT * FROM profiles WHERE university = ?"
    cursor.execute(find_someone, [(uni)])
    exist = cursor.fetchall()

    usernames = []
    for each in exist:
        usernames.append(each[1])

    if len(exist) > 0:
        print("Users at University ", uni, ": ")
        for user in exist:
            print("Username: ", user[1])

        if wantSendRequest() == True:
            requested = single_line_alphaNumString("Enter their username: ")
            if requested in usernames:
                friend_request(me, requested)
            else:
                print("That isn't one of the usernames.")

    else:
        print("There is nobody attending that university")


def listByMajor(me):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    major = input("Enter Major: ").title()
    # Check if user is in system
    find_someone = "SELECT * FROM profiles WHERE major = ?"
    cursor.execute(find_someone, [(major)])
    exist = cursor.fetchall()

    usernames = []
    for each in exist:
        usernames.append(each[1])

    if len(exist) > 0:
        print("Users with major ", major, ": ")
        for user in exist:
            print("Username: ", user[1])

        if wantSendRequest() == True:
            requested = single_line_alphaNumString("Enter their username: ")
            if requested in usernames:
                friend_request(me, requested)
            else:
                print("That isn't one of the usernames.")

    else:
        print("There is nobody with that major")


def login_credentials():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    username = single_line_alphaString("\nUsername: ")
    password = single_line_string("Password: ")

    find_user = "SELECT * FROM user WHERE username = ? AND password = ?"
    cursor.execute(find_user, [(username), (password)])
    results = cursor.fetchall()

    if results:
        return [True, username]
    else:
        return [False]


def createUserProfile(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if there are 3 user jobs already
    jobs_count = ("SELECT * FROM profiles WHERE username = ?")
    cursor.execute(jobs_count, [(username)])
    number = cursor.fetchall()

    if (len(number)) > 0:
        print(
            "You already have a Profile, but you can use the Edit Option!"
        )
    else:
        title = (input("Enter your title (E.g., Student): ")).title()
        major = (input("Enter your major: ")).title()
        university = (input("Enter your University: ")).title()
        about = mutli_line_string("Write Your About Section: ")

        cursor.execute(
            """
        INSERT INTO profiles (username, title, major, university, about) VALUES(?,?,?,?,?)""",
            (username, title, major, university, about),
        )
        db.commit()
        print("Your profile has been created.")


def editUserProfile(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if they already have created a profile
    profile_count = ("SELECT * FROM profiles WHERE username = ?")
    cursor.execute(profile_count, [(username)])
    number = cursor.fetchall()

    print("Length of profiles: ", len(number))
    for i in number:
        print("CHECKING: ", i)

    if (len(number)) == 0:
        print(
            "You haven't created a profile yet!"
        )
    else:
        print(ui.edit_profile_menu)
        edit_option = integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while (edit_option != 5):

            if edit_option == 1:
                change = (input("Enter your title (E.g., Student): ")).title()
                update = ''' UPDATE profiles SET title = ? WHERE username = ?'''

            elif edit_option == 2:
                change = (input("Enter your major: ")).title()
                update = ''' UPDATE profiles SET major = ? WHERE username = ?'''

            elif edit_option == 3:
                change = (input("Enter your University: ")).title()
                update = ''' UPDATE profiles SET university = ? WHERE username = ?'''

            else:
                change = mutli_line_string("Enter your University: ")
                update = ''' UPDATE profiles SET about = ? WHERE username = ?'''

            cursor.execute(update, [(change, username)])
            db.commit()

            print(ui.edit_profile_menu)
            edit_option = integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)


def createEducation(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if there are 3 user jobs already
    edu = ("SELECT * FROM education WHERE username = ?")
    cursor.execute(edu, [(username)])
    number = cursor.fetchall()

    if (len(number)) > 0:
        print(
            "You already have an Education Section, use the editing option!"
        )
    else:
        school = (input("School Name: ")).title()
        degree = (input("Enter your Degree: ")).title()
        years = integer("Full Years Attended to Date: ")

        cursor.execute(
            """
        INSERT INTO education (username, school, degree, years) VALUES(?,?,?,?)""",
            (username, school, degree, years),
        )
        db.commit()
        print("Your education section has been created.")


def editEducation(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if they already have created an education section
    edu_count = ("SELECT * FROM education WHERE username = ?")
    cursor.execute(edu_count, [(username)])
    number = cursor.fetchall()

    if (len(number)) == 0:
        print(
            "You haven't created an education section yet!"
        )
    else:
        print(ui.edit_education_menu)
        edit_option = integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while (edit_option != 4):

            if edit_option == 1:
                change = (input("School Name: ")).title()
                update = ''' UPDATE education SET school = ? WHERE username = ?'''

            elif edit_option == 2:
                change = (input("Enter your Degree: ")).title()
                update = ''' UPDATE education SET degree = ? WHERE username = ?'''

            elif edit_option == 3:
                change = integer("Full Years Attended to Date: ")
                update = ''' UPDATE education SET years = ? WHERE username = ?'''

            cursor.execute(update, [change, username])
            db.commit()

            print(ui.edit_education_menu)
            edit_option = integer_in_range("Enter which to edit: ", 1, 5, ui.edit_education_menu)


def createJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if there are 3 user jobs already
    jobs_count = ("SELECT * FROM jobs WHERE username = ?")
    cursor.execute(jobs_count, [(username)])
    number = cursor.fetchall()

    if (len(number)) >= 4:
        print(
            "All Permitted Jobs Have Been Created for Your Account"
        )
    else:
        title = (single_line_string("Enter your Title (E.g., Student): ")).title()
        employer = (single_line_string("Enter your Employer: ")).title()
        started = single_line_string("Enter Your Start Date: ")
        ended = single_line_string("Enter Your End Date: ")
        location = (single_line_string("Enter Location of Job: ")).title()
        description = mutli_line_string("Enter Description: ")

        cursor.execute(
            """
        INSERT INTO jobs (username, title, employer, started, ended, location, description) VALUES(?,?,?,?,?,?,?)""",
            (username, title, employer, started, ended, location, description),
        )
        db.commit()
        print("Your job has been created.")


def editJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if they already have created a profile
    job_count = ("SELECT * FROM jobs WHERE username = ?")
    cursor.execute(job_count, [(username)])
    number = cursor.fetchall()

    print("Length of jobs: ", len(number))

    if (len(number)) == 0:
        print(
            "You haven't created a job yet!"
        )
    else:
        displayUserJob(username)
        jobTitle = chooseJob(username)

        print(ui.edit_job_menu)
        edit_option = integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while (edit_option != 7):

            if edit_option == 1:
                change = title = (single_line_string("Enter your Title (E.g., Student): ")).title()
                update = ''' UPDATE jobs SET title = ? WHERE username = ? AND title = ?'''

            elif edit_option == 2:
                change = employer = (single_line_string("Enter your Employer: ")).title()
                update = ''' UPDATE jobs SET employer = ? WHERE username = ? AND title = ?'''

            elif edit_option == 3:
                change = single_line_string("Enter Your Start Date: ")
                update = ''' UPDATE jobs SET started = ? WHERE username = ? AND title = ?'''

            if edit_option == 4:
                change = single_line_string("Enter Your End Date: ")
                update = ''' UPDATE jobs SET ended = ? WHERE username = ? AND title = ?'''

            elif edit_option == 5:
                change = (single_line_string("Enter Location of Job: ")).title()
                update = ''' UPDATE jobs SET location = ? WHERE username = ? AND title = ?'''

            elif edit_option == 6:
                change = mutli_line_string("Enter Description: ")
                update = ''' UPDATE jobs SET description = ? WHERE username = ? AND title = ?'''

            cursor.execute(update, [change, username, jobTitle])
            db.commit()

            print(ui.edit_job_menu)
            edit_option = integer_in_range("Enter which to edit: ", 1, 7, ui.edit_job_menu)


def chooseJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if they already have created a profile
    job_count = ("SELECT * FROM jobs WHERE username = ?")
    cursor.execute(job_count, [(username)])
    number = cursor.fetchall()

    print("Select One of the Following to Edit: ")
    for result in number:
        print(result[0], ". ", result[2])

    choice = integer_in_range("Select One of the Jobs to Edit by number: ", 1, len(number), "NULL")
    return (number[choice - 1][2])


def displayUser(me, username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_user = "SELECT * FROM profiles WHERE username = ?"
    cursor.execute(find_user, [(username)])
    profiles = cursor.fetchall()

    find_user = "SELECT * FROM education WHERE username = ?"
    cursor.execute(find_user, [(username)])
    education = cursor.fetchall()

    find_user = "SELECT * FROM jobs WHERE username = ?"
    cursor.execute(find_user, [(username)])
    jobs = cursor.fetchall()

    if checkFriends(me, username):

        if len(profiles) > 0:
            displayUserProfile(username)
            if len(education) > 0:
                displayUserEducation(username)
            if len(jobs) > 0:
                displayUserJob(username)

    else:
        print("You are not friends with them to view their profile")


def displayUserProfile(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_user = "SELECT * FROM user WHERE username = ?"
    cursor.execute(find_user, [(username)])
    users = cursor.fetchall()

    find_profile = "SELECT * FROM profiles WHERE username = ?"
    cursor.execute(find_profile, [(username)])
    profiles = cursor.fetchall()

    for user in users:
        print("\n---------- You are viewing ", user[3], user[4], "'s profile ----------")
        print("Title: ", profiles[0][2])
        print("Major: ", profiles[0][3])
        print("University: ", profiles[0][4])
        print("About: : ", profiles[0][5])


def displayUserJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_job = "SELECT * FROM jobs WHERE username = ?"
    cursor.execute(find_job, [(username)])
    results = cursor.fetchall()

    for job in results:
        print("\n---------- Jobs ----------")
        print("Title: ", job[2])
        print("Employer: ", job[3])
        print("Date Started: ", job[4])
        print("Date Ended: ", job[5])
        print("Location: ", job[6])
        print("Description of Job: ", job[7])


def displayUserEducation(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_edu = "SELECT * FROM education WHERE username = ?"
    cursor.execute(find_edu, [(username)])
    results = cursor.fetchall()

    for education in results:
        print("---------- Education ----------")
        print("School: ", education[2])
        print("Degree: ", education[3])
        print("Years Attended: ", education[4])


def listAllUsers():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()

    print("Existing Accounts:")
    number = 1
    for i in results:
        print(f"  {number}: {i[1]}")
        number = number + 1

    cursor.close()


# the user sends request to stranger
def friend_request(me, stranger):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    # if a print input needed:
    # stranger = single_line_alphaString("Enter Username you want to send request:")

    # check if target user is available
    if checkUsernameExists(stranger) == False:
        print("The username you try to add as friend does not exist.")
        return

    # check if me already sent request
    find_request = "SELECT * FROM friends WHERE username = ? AND stranger = ?"
    cursor.execute(find_request, [(me), (stranger)])
    exist = cursor.fetchall()
    if len(exist) > 0:
        print("You've already sent a friend request to this user.")
        db.close()
        return

    # both users' status updated to pending
    cursor.execute(
        """
    INSERT INTO friends (username, stranger, status) VALUES(?,?,'sentpending')""",
        (me, stranger),
    )
    cursor.execute(
        """
    INSERT INTO friends (username, stranger, status) VALUES(?,?,'acceptpending')""",
        (stranger, me),
    )
    db.commit()
    print("You Have sent friend request to", stranger)
    db.close()


# 1. Reject: delete both table
# 2. Accept: Update both status to friend
def exec_friend_request(me):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_acceptRequests = "SELECT * FROM friends WHERE username = ? AND status = 'acceptpending'"
    cursor.execute(find_acceptRequests, [(me)])
    results = cursor.fetchall()

    for sent in results:

        stranger = sent[1]
        print("\nWould you like to accept friend request from", stranger)
        FriendChoice = integer_in_range(
            "Enter 1 to Accept and 2 to Reject: ", 1, 2, "NULL"
        )
        if FriendChoice == 2:
            # delete both users' request from db
            reject_request = "DELETE * FROM friends WHERE username = ? AND stranger = ?"
            cursor.execute(reject_request, [(me), (stranger)])
            reject_request2 = "DELETE * FROM friends WHERE username = ? AND stranger = ?"
            cursor.execute(reject_request2, [(stranger), (me)])
            db.commit()
            print("You have rejected friend request from", stranger)
            db.close()
        else:
            # both change status to "friend"
            reject_request1 = ''' UPDATE friends SET status = ? WHERE username = ? AND stranger = ?'''
            cursor.execute(reject_request1, [("friend"), (me), (stranger)])
            reject_request2 = ''' UPDATE friends SET status = ? WHERE username = ? AND stranger = ?'''
            cursor.execute(reject_request2, [("friend"), (stranger), (me)])
            db.commit()
            print("You have accepted friend request from,", stranger)
            db.close()


def delete_friend(me, stranger):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    # delete both users' request from db
    reject_request = "DELETE FROM friends WHERE username = ? AND stranger = ?"
    cursor.execute(reject_request, [(me), (stranger)])
    reject_request2 = "DELETE FROM friends WHERE username = ? AND stranger = ?"
    cursor.execute(reject_request2, [(stranger), (me)])
    db.commit()
    print("You have removed ", stranger)
    db.close()


def listPending(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_sentRequests = "SELECT * FROM friends WHERE username = ? AND status = 'sentpending'"
    cursor.execute(find_sentRequests, [(username)])
    results = cursor.fetchall()

    print("Your Outgoing Friend Requests: \n")
    for sent in results:
        print(sent[0])

    find_acceptRequests = "SELECT * FROM friends WHERE username = ? AND status = 'acceptpending'"
    cursor.execute(find_acceptRequests, [(username)])
    results = cursor.fetchall()

    print("Your Incoming Friend Requests: \n")
    for sent in results:
        print(sent[0])


def listFriends(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_friends = "SELECT * FROM friends WHERE username = ? AND status = 'friend'"
    cursor.execute(find_friends, [(username)])
    results = cursor.fetchall()

    usernames = []
    for each in results:
        usernames.append(each[1])

    if len(results) > 0:
        print("Your Friends:")
        for sent in results:
            print("     ", sent[1])

        if wantDeleteFriend() == True:
            requested = single_line_alphaNumString("Enter their username: ")
            if requested in usernames:
                delete_friend(username, requested)
            else:
                print("That isn't one of the usernames.")
    else:
        print("You don't have any connections.")


def checkFriends(username, friend):
    print("Check friends: ", username, friend)
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_friends = "SELECT * FROM friends WHERE username = ? AND status = 'friend'"
    cursor.execute(find_friends, [(username)])
    results = cursor.fetchall()

    if len(results) > 0:
        return True
    else:
        return False


def pending_friend(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_pending = "SELECT * FROM friends WHERE username = ? AND status = 'acceptpending'"
    cursor.execute(find_pending, [(username)])
    pending = cursor.fetchall()
    if len(pending) > 0:
        return True
        # db.close()
    else:
        return False
        # db.close()


#### EPIC 6 ####
def deleteJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if they already have created a profile
    job_count = ("SELECT * FROM jobs WHERE username = ?")
    cursor.execute(job_count, [(username)])
    number = cursor.fetchall()

    print("Number of jobs: ", len(number))

    if (len(number)) == 0:
        print(
            "You haven't created a job yet!"
        )
    else:
        displayUserJob(username)
        # jobTitle = chooseJob_forD(username) #it's jobs' title
        print("Select One of the Following to Delete: ")
        a = 1
        for result in number:
            print(a, ". ", result[2])
            a = a + 1
        choice = integer_in_range("Select One of the Jobs to Delete by number: ", 1, len(number), "NULL")
        jobTitle = (number[choice - 1][2])  # number 2d list
        # choose which job here

        # 1. delete job from jobs talble
        # 2. updated status for apply table
        delete_job = "DELETE FROM jobs WHERE username = ? AND title = ?"
        cursor.execute(delete_job, [(username), (jobTitle)])
        db.commit()

        find_status = "SELECT * FROM applyInfo WHERE title = ?"
        cursor.execute(find_status, [(jobTitle)])
        find_results = cursor.fetchall()

        if len(find_results) > 0:
            update_status = ''' UPDATE applyInfo SET status = ? WHERE title = ?'''
            cursor.execute(update_status, [("deleted"), (jobTitle)])
            db.commit()

        print("This job has been deleted: ", jobTitle)
        db.close()


def deletion_detector(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_deleted = "SELECT * FROM applyInfo WHERE username = ? AND status = 'deleted'"
    cursor.execute(find_deleted, [(username)])
    deleted = cursor.fetchall()
    if len(deleted) > 0:
        print("NOTIFICATION: Unfortunately, following job(s) you applied for has been deleted by the publisher: ")
        for job in deleted:
            print("Title: ", job[1])
        # db.close()


def listJobsApplied(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_JobsApplied = "SELECT * FROM applyInfo WHERE username = ? AND status = 'applied'"
    cursor.execute(find_JobsApplied, [(username)])
    results = cursor.fetchall()

    print("Your applied jobs: \n")
    for applied in results:
        print("Title: ", applied[1])
        # print("Publisher: ", applied[1])

def CountJobsApplied(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_JobsApplied = "SELECT * FROM applyInfo WHERE username = ? AND status = 'applied'"
    cursor.execute(find_JobsApplied, [(username)])
    results = cursor.fetchall()

    job_count = 0
    print("Your applied jobs: \n")
    for applied in results:
        job_count = job_count + 1;
        # print("Title: ", applied[1])
        # print("Publisher: ", applied[1])
    return job_count


def unsaveJob(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    choice2 = integer_in_range("\nDo you want to unsave any job in your list?"
                               "\n1. Unsave the job"
                               "\n2. Back to main menu"
                               "\nType 1 or 2 here: ", 1, 2, "NULL")
    if choice2 == 1:
        title1 = (single_line_string("Enter your Title you want to unsave: ")).title()

        delete_save = "DELETE FROM applyInfo WHERE username = ? AND title = ? AND status = 'saved'"
        cursor.execute(delete_save, [(username), (title1)])
        db.commit()

        print("This job has been unsaved!")
        db.close()


def listJobsSaved(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_JobsSaved = "SELECT * FROM applyInfo WHERE username = ? AND status = 'saved'"
    cursor.execute(find_JobsSaved, [(username)])
    results = cursor.fetchall()

    if len(results) > 0:
        print("Your saved jobs: \n")
        for saved in results:
            print("Title: ", saved[1])
            unsaveJob(username)
    else:
        print("You haven't saved any job!")


def listJobsNotApplied(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_JobsApplied = "SELECT * FROM applyInfo WHERE username = ? AND status = 'applied'"
    cursor.execute(find_JobsApplied, [(username)])
    results = cursor.fetchall()
    AppliedJobs = []
    for applied in results:
        AppliedJobs.append(applied[1])  # applied job's title

    cursor.execute("SELECT * FROM jobs")
    job_results = cursor.fetchall()
    AllJobs = []
    for each in job_results:
        AllJobs.append(each[2])  # all jobs' title

    # NotApplied = []
    # NotApplied = list(set(AppliedJobs).difference(set(AllJobs)))  # difference AppliedJobs
    NotApplied = [i for i in AllJobs if i not in AppliedJobs]
    print("Your not applied jobs: \n")
    for x in NotApplied:
        print("Title: ", x)

    # db.close()


def applyJob(username):
    # display all jobs, ask student if they want to apply for this job
    # 3 checks:
    # if they select that job, ask student to enter info
    # if they select that job, if they have created that job, print "cannot apply"
    # if they select that job, if they have already applied, print "already applied" and cannot apply again
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()
    apply_job = ("SELECT * FROM jobs")
    cursor.execute(apply_job)
    number = cursor.fetchall()

    if (len(number)) > 0:
        a = 1
        for job in number:
            print(a, ".", job[2])
            a = a + 1
        choice = integer_in_range("\nSelect One of the Jobs by number to apply for: ", 1, len(number), "NULL")
        # if already applied
        apply_job = ("SELECT * FROM applyInfo WHERE username = ? AND title = ? AND status = 'applied'")
        cursor.execute(apply_job, [(username), (number[choice - 1][2])])
        number2 = cursor.fetchall()

        if (len(number2)) > 0:
            print("You have already applied, try applying for another job.")
        elif (username == number[choice - 1][1]):  # if they have created job, they cant apply
            print(
                "You cannot apply to a job you have created yourself, try applying for another job that you haven't created.")
        else:
            # title = (single_line_string("Enter the title of the job: ")).title()
            graduateDate = single_line_string("Enter the graduation date: ")
            startDate = single_line_string("Enter the date you can start working: ")
            explaining = mutli_line_string("Enter why you would be a good fit for this job: ")

            cursor.execute(
                """
            INSERT INTO applyInfo (username, title, graduateDate, startDate, explaining, status) VALUES(?,?,?,?,?,'applied')""",
                (username, number[choice - 1][2], graduateDate, startDate, explaining),
            )
            db.commit()
            print("Your applied jobs info has been created.")
            db.close()


def saveJob(username, choice):
    # display all jobs, ask student if they want to apply for this job
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_job = "SELECT * FROM jobs"
    cursor.execute(find_job)
    results = cursor.fetchall()

    choice2 = integer_in_range("\nDo you want to save this job to your list?"
                               "\n1. Save the job"
                               "\n2. Back to main menu"
                               "\nType 1 or 2 here: ", 1, 2, "NULL")
    if choice2 == 1:
        find_savedjob = "SELECT * FROM applyInfo WHERE username = ? AND title = ? AND status ='saved'"
        cursor.execute(find_savedjob, [(username), (results[choice - 1][1])])
        st = cursor.fetchall()
        if len(st) > 0:
            print("You have already saved it")
        else:
            cursor.execute(
                """
            INSERT INTO applyInfo (username, title, status) VALUES(?,?,'saved')""",
                (username, results[choice - 1][2]),
            )
            db.commit()
            print("The job is saved!")


def jobBoard(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    jobs_board = ("SELECT * FROM jobs")
    cursor.execute(jobs_board)
    number = cursor.fetchall()

    deletion_detector(username)  # notification

    # prints all the titles of the job in system and how many jobs user applied
    #cursor.execute("SELECT COUNT(*) FROM jobs WHERE username=?", (username,))
    #applied_jobs = cursor.fetchone();
    job_counter = CountJobsApplied(username)
    # print(applied_jobs)
    #for a in applied_jobs:
        #if a == 1:
            #job_counter += 1

    print("############# Job Board #############")
    print("You have currently applied for", job_counter, "jobs")  ######## EPIC 8 ########
    if (len(number)) == 0:
        print("No job been posted")
    else:
        a = 1
        for job in number:  # change this to just print out the selected job not all jobs
            print(a, ".", job[2])
            a = a + 1

        choice = integer_in_range("\nSelect One of the Jobs by number to learn more about: ", 1, len(number), "NULL")
        print("Title: ", number[choice - 1][2])
        print("Employer: ", number[choice - 1][3])
        print("Date Started: ", number[choice - 1][4])
        print("Date Ended: ", number[choice - 1][5])
        print("Location: ", number[choice - 1][6])
        print("Description of Job: ", number[choice - 1][7])
        saveJob(username, choice)


#### END OF EPIC 6 ####


######## EPIC 7 ########

# can SEND and RECEIVE messages from people who have accepted their friend request
def standardTier(sender, receiver):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    # Checking if they have them as a friend
    find_friends = "SELECT * FROM friends WHERE username = ? AND stranger = ? AND status = 'friend'"
    cursor.execute(find_friends, [(sender), (receiver)])
    results = cursor.fetchall()

    # Generate list of all the Incollege members who are their friends
    usernames = []
    for each in results:
        usernames.append(each[1])

    if len(results) > 0:
        print("These are your friends that you can message:")
        for sent in results:
            print("     ", sent[1])

        chatInput = input("Enter your message: ")

        cursor.execute(
            """
        INSERT INTO messageFriend (sender, receiver, message, status) VALUES(?,?,?,'sent')""",
            (receiver, sender, chatInput),
        )

        db.commit()
        print("You Have sent the message to", receiver)
        db.close()
    else:
        print("I'm sorry, you are not friends with that person.")


# can SEND and RECIEVE messages from people who have accepted their friend request
# can also SEND and RECEIVE messages from people not in thier friend list

def plusTier(sender):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    EveryOne = "SELECT * FROM user EXCEPT SELECT * FROM user WHERE username = ?"
    cursor.execute(EveryOne, [(sender)])
    results = cursor.fetchall()

    usernames = []
    for each in results:
        usernames.append(each[1])

    if len(results) > 0:
        print("These are the users that you can message:")
        for sent in results:
            print("     ", sent[1])
        user = input("Enter the user you want to message: ")
        chatInput = input("Enter your message: ")

        cursor.execute(
            """
            INSERT INTO messageFriend (sender, receiver, message, status) VALUES(?,?,?,'sent')""",
            (user, sender, chatInput),
        )

        db.commit()
        print("You Have sent the message to", user)
        db.close()
    else:
        print("Please try again.")


##### epic 8

# Message notification
def message_detector(sender, receiver):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_message = "SELECT * FROM messageFriend WHERE sender = ? AND status = 'sent'"
    cursor.execute(find_message, [(sender)])
    results = cursor.fetchall()
    for msg in results:
        who = msg[1]
        print("NOTIFICATION: You have received a message from", who)

        readMsg = integer_in_range("\nDo you want to read the message?"
                                   "\n1. Read the message"
                                   "\n2. Back to main menu"
                                   "\nType 1 or 2 here: ", 1, 2, "NULL")
        if readMsg == 1:
            print("Message: ", msg[2])  # display message
        else:
            main()

        ## this part give user option (1 = leave it as it is, 3 = delete message from messsageTable, 2 = send message back)
        msgChoice = integer_in_range("Enter 1 to leave the message, 2 to send message back, 3 to delete the message: ",
                                     1, 3, "NULL")
        if msgChoice == 3:
            # delete the message from db
            reject_message = "DELETE FROM messageFriend WHERE sender = ?"
            cursor.execute(reject_message, [(sender)])
            db.commit()
            print("You have removed the message from your inbox")
            db.close()
            main()
        elif msgChoice == 2:
            friend = input("Name of the friend to send a message to: ")
            chatInput = input("Enter your message: ")

            cursor.execute(
                """
                INSERT INTO messageFriend (sender, receiver, message, status) VALUES(?,?,?,'sent')""",
                (friend, sender, chatInput),
            )

            db.commit()
            print("You Have sent the message to", friend)
            reject_message = "DELETE FROM messageFriend WHERE sender = ?"
            cursor.execute(reject_message, [(sender)])
            db.commit()
            main()
            message_detector(sender, receiver)
        else:
            print("You have left the message inside of your inbox. Come back again!")
            main()


def pending_message(username):
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    find_pending = "SELECT * FROM messageFriend WHERE sender = ? AND status = 'sent'"
    cursor.execute(find_pending, [(username)])
    pending = cursor.fetchall()
    if len(pending) > 0:
        return True
        # db.close()
    else:
        return False
        # db.close()


def pending_profile(temp):  # temp = username

    # check if the user has a profile or not
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    # serches for if the user has a profile or not 
    find_profile = "SELECT * FROM profiles WHERE username = ?"
    cursor.execute(find_profile, [(temp)])
    users = cursor.fetchall()

    # searches for if the profile has an existing timer or not
    find_timed_profile = "SELECT * FROM profileTimer WHERE username = ?"
    cursor.execute(find_timed_profile, [(temp)])
    timedOne = cursor.fetchall()

    # user does not have an existing profile
    if len(users) == 0:

        # check if the user's profile is timed or not
        # the profile is timed. check the difference
        if len(timedOne) != 0:

            present = datetime.date.today()  # today's date
            cursor.execute(
                """INSERT INTO profileTimer (username,startTime) VALUES(?,?)""",
                (temp, present),
            )

            # there is a timed profile present
        elif len(timedOne) > 0:
            # compare timings on the present
            now = datetime.date.today()  # this is time (in seconds) now
            find_time_from_timedProfile = "SELECT startTime FROM profileTimer WHERE username = ?"
            cursor.execute(find_time_from_timedProfile, [(temp)])
            then = cursor.fetchall()  # this is the time saved the first time

            # if the difference is 7 days then print the reminder
            if (now - then == 7):
                print(
                    "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

    else:
        return True


######################################################################################################## UI Functions

def login_menu():
    print(ui.main_menu)
    choice = integer_in_range("Choice: ", 1, 5, ui.main_menu)
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
    print(ui.guest_controls_menu)
    choice = integer_in_range("Choose which to toggle: ", 1, 4, ui.guest_controls_menu)

    while choice != 4:
        if choice == 1:
            print("Emails have been toggled.")
        if choice == 2:
            print("SMS have been toggled.")
        if choice == 3:
            print("Targeted Ads have been toggled.")
        if choice == 4:
            return 0

        print(ui.guest_controls_menu)
        choice = integer_in_range("Choose which to toggle: ", 1, 4, ui.guest_controls_menu)


###################################################################################################################################### Input Validation Functions


def integer_in_range(prompt, low, high, menu):
    number = input(prompt)

    while (not number.isnumeric()) or (int(number) < low) or (int(number) > high):
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


def wantSendRequest():
    string_in = input("Would you like to send a friend request? (Yes / No): ")
    acceptable = ["yes", "y", "no", "n"]

    while (not string_in.isalpha()) or (string_in.lower() not in acceptable):
        print("\nPlease type a valid response.\n")
        string_in = input("Would you like to send a friend request? (Yes / No): ")

    if string_in.lower() == "yes" or string_in.lower() == "y":
        return True
    else:
        return False


def wantDeleteFriend():
    string_in = input("Would you like to remove a connection? (Yes / No): ")
    acceptable = ["yes", "y", "no", "n"]

    while (not string_in.isalpha()) or (string_in.lower() not in acceptable):
        print("\nPlease type a valid response.\n")
        string_in = input("Would you like to remove a connection? (Yes / No): ")

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
# def clear():
#     os.system("cls" if os.name == "nt" else "clear")

################################################################################################################################## Main Function

def main():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()

    ##### Main Menu
    print(ui.success_story)
    option = login_menu()

    ##### Handle Main Menu Choice

    ## Login to Account
    if option == 1:
        listAllUsers()

        TryAgain = True
        while TryAgain == True:
            LoggedIn = login_credentials()
            if LoggedIn[0]:
                TryAgain = False
            else:
                TryAgain = tryAgain()

        if LoggedIn[0]:
            temp = LoggedIn[1]  # [true][username]  temp = username  #
            temp1 = "string"
            if pending_friend(LoggedIn[1]):
                print("You received a friend request.")
                exec_friend_request(LoggedIn[1])
            elif pending_message(temp):
                print("You have received a message in your inbox.")
                message_detector(temp, temp1)
            elif pending_profile(temp):
                # print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
                # redirect to create a profile

                print(ui.logged_in_menu)
            print(ui.logged_in_menu)
            choice = integer_in_range("Pick an Option: ", 1, 21, ui.logged_in_menu)
            while choice != 21:

                if choice == 1:  # Search for a Job / Internship
                    jobBoard(LoggedIn[1])

                elif choice == 2:  # Apply for a Job
                    applyJob(LoggedIn[1])

                elif choice == 3:  # List of Applied / Not-Applied Jobs
                    print(ui.list_job_menu)
                    search_choice = integer_in_range("Select what you would like to search by: ", 1, 3,
                                                     ui.list_job_menu)
                    while search_choice != 3:
                        if search_choice == 1:
                            listJobsApplied(LoggedIn[1])

                        elif search_choice == 2:
                            listJobsNotApplied(LoggedIn[1])

                        print(ui.list_job_menu)
                        search_choice = integer_in_range("Select what you would like to search by: ", 1, 3, "NULL")

                elif choice == 4:  # List of Saved Jobs / Unsave a Job
                    listJobsSaved(LoggedIn[1])

                elif choice == 5:  # Find Someone That You May Know
                    print(ui.search_menu)
                    search_choice = integer_in_range("Select what you would like to search by: ", 1, 5, "NULL")
                    while (search_choice != 5):
                        if search_choice == 1:
                            checkNameExists(LoggedIn[1])
                        elif search_choice == 2:
                            listByLastName(LoggedIn[1])

                        elif search_choice == 3:
                            listByUniversity(LoggedIn[1])

                        elif search_choice == 4:
                            listByMajor(LoggedIn[1])

                        print(ui.search_menu)
                        search_choice = integer_in_range("Select what you would like to search by: ", 1, 5, "NULL")

                elif choice == 6:  # Learn a New Skill
                    print(ui.skills_menu)
                    skills_choice = integer_in_range(
                        "Pick an Option: ", 1, 6, ui.skills_menu
                    )

                    while skills_choice != 6:
                        skills(skills_choice)

                        print(ui.skills_menu)
                        skills_choice = integer_in_range(
                            "Pick an Option: ", 1, 6, ui.skills_menu
                        )

                elif choice == 7:  # InCollege Important Links
                    print(ui.important_links_menu)
                    option = integer_in_range(
                        "Please choose an option to learn about: ",
                        1,
                        10,
                        ui.important_links_menu,
                    )
                    while option != 10:
                        importantLinks(option)
                        print(ui.important_links_menu)
                        option = integer_in_range(
                            "Please choose an option to learn about: ",
                            1,
                            10,
                            ui.important_links_menu,
                        )

                elif choice == 8:  # Useful Links
                    usefulLinks()

                elif choice == 9:  # Create Your User Profile
                    createUserProfile(LoggedIn[1])

                elif choice == 10:  # Create Education
                    createEducation(LoggedIn[1])

                elif choice == 11:  # Create a Job
                    createJob(LoggedIn[1])

                elif choice == 12:  # Edit Your User Profile
                    editUserProfile(LoggedIn[1])

                elif choice == 13:  # Edit Your Education
                    editEducation(LoggedIn[1])

                elif choice == 14:  # Edit Jobs
                    editJob(LoggedIn[1])

                elif choice == 15:  # Delete Jobs
                    deleteJob(LoggedIn[1])

                elif choice == 16:  # Display a User Profile
                    userRequested = single_line_alphaString(
                        'Type the username of the user you want to see the profile for or "exit" to return: '
                    )
                    while (
                            not checkUsernameExists(userRequested)
                    ) and userRequested.lower() != "exit":
                        print(
                            "That username isn't in the system. Try Again or type exit to leave.\n"
                        )
                        userRequested = single_line_alphaString(
                            'Type the username of the user you want to see the profile for or "exit" to return: '
                        )

                    if userRequested.lower() != "exit":
                        displayUser(LoggedIn[1], userRequested)

                elif choice == 17:  # Send a Friend Request
                    stranger = single_line_alphaNumString("Enter the username of the user you want to friend: ")
                    friend_request(LoggedIn[1], stranger)

                elif choice == 18:  # List Pending Requests
                    listPending(LoggedIn[1])

                elif choice == 19:  # Show My Network
                    listFriends(LoggedIn[1])
                elif choice == 20:  # Message
                    print(ui.message_menu)
                    search_choice = integer_in_range(
                        "Enter 1 as a Standard member, Enter 2 as a Plus member, Enter 3 to go back: ", 1, 3,
                        ui.message_menu)
                    while search_choice != 3:
                        if search_choice == 1:
                            receiver = single_line_alphaNumString(
                                "Enter the username of the user you want to send a message to: ")
                            standardTier(LoggedIn[1], receiver)
                        elif search_choice == 2:
                            # receiver = single_line_alphaNumString("Enter the username of the user you want to send a message to: ")
                            # plusTier(LoggedIn[1], receiver)
                            plusTier(LoggedIn[1])
                        print(ui.message_menu)
                        search_choice = integer_in_range("Select what you would like to search by: ", 1, 3, "NULL")

                print(ui.logged_in_menu)
                choice = integer_in_range(
                    "Pick an Option: ", 1, 21, ui.logged_in_menu
                )

        print("Goodbye, Have a Nice Day !")
        raise SystemExit(0)

    ## Create an Account
    if option == 2:
        createAccount()
        main()

    if option == 3:
        print(ui.important_links_menu)
        option = integer_in_range(
            "Please choose an option to learn about: ", 1, 10, ui.important_links_menu
        )
        if option != 10:
            importantLinks(option)
        else:
            main()

    if option == 4:
        usefulLinks()
        main()

    if option == 5:
        exit()


if __name__ == "__main__":
    main()
