import sqlite3
from sqlite3.dbapi2 import connect
import ui

##### Create the Database if it doesn't exist
with sqlite3.connect("User.db") as db:
    cursor = db.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username   VARCHAR(20) NOT NULL,
password   VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name  VARCHAR(20) NOT NULL); 
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS profiles(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
title VARCHAR(20),
major VARCHAR(20),
university VARCHAR(50),
about VARCHAR(250));
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS jobs(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
title VARCHAR(20),
employer VARCHAR(20),
started VARCHAR(20),
ended VARCHAR(20),
location VARCHAR(20),
description VARCHAR(250));
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS education(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
school VARCHAR(50),
degree VARCHAR(50),
years INTEGER);
"""
)

cursor.close()
###################################################
# run this file if you want to empty the database #
###################################################


def createAccount():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    ## Checking if there are 5 user accounts already
    cursor.execute("SELECT COUNT(*) FROM user")
    number = cursor.fetchall()

    if (len(number)) >= 6:
        print(
            "All Permitted Accounts Have Been Created, Please Log in if You Have an Account."
        )

    else:
        username = ui.single_line_alphaString("Enter Username:")
        while checkUsernameExists(username):
            print("\nAn Account of that username exists, Try Again.\n")
            username = ui.single_line_alphaString("Enter Username:")

        password = ui.single_line_string("Enter Account Password: ")
        while not ui.checkPasswordWorks(password):
            password = ui.single_line_string("Enter Account Password: ")

        firstName = ui.single_line_alphaNumString("Enter First Name: ")
        lastName = ui.single_line_alphaNumString("Enter Last Name: ")

        cursor.execute(
            """
        INSERT INTO user (username,password, first_name, last_name) VALUES(?,?,?,?)""",
            (username, password, firstName, lastName),
        )
        db.commit()

        print("You Have Registered", username)


# def createNewUser(username, password, firstName, lastName):

#     # process to create a new account
#     with sqlite3.connect("User.db") as db:
#         cursor = db.cursor()

#     cursor.execute(
#         """
#     INSERT INTO user (username,password, first_name, last_name) VALUES(?,?,?,?)""",
#         (username, password, firstName, lastName),
#     )
#     db.commit()

#     print("You Have Registered", username)


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


def checkNameExists():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    # Check if user is in system
    find_someone = "SELECT * FROM user WHERE first_name = ? AND last_name = ?"
    cursor.execute(find_someone, [(first), (last)])
    exist = cursor.fetchall()

    if len(exist) > 0:
        print("They are a part of the InCollege System")
    else:
        print("They are not yet a part of the InCollege system yet")


def login_credentials():
    with sqlite3.connect("User.db") as db:
        cursor = db.cursor()

    username = ui.single_line_alphaString("\nUsername: ")
    password = ui.single_line_string("Password: ")

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
        about = ui.mutli_line_string("Write Your About Section: ")

        cursor.execute(
            """
        INSERT INTO profiles (username, title, major, university, about) VALUES(?,?,?,?,?)""",
            (username, title, major, university, about),
            )
        db.commit()

        print("You Have Entered in profile: ", title)

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
        edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while(edit_option != 5):

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
                change = ui.mutli_line_string("Enter your University: ")
                update = ''' UPDATE profiles SET about = ? WHERE username = ?'''

            cursor.execute(update, [(change, username)])
            db.commit()

            print(ui.edit_profile_menu)
            edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)


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
        years = ui.integer("Full Years Attended to Date: ")

        cursor.execute(
            """
        INSERT INTO education (username, school, degree, years) VALUES(?,?,?,?)""",
            (username, school, degree, years),
            )
        db.commit()

        print("You Have Entered in profile: ", school)

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
        edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while(edit_option != 4):

            if edit_option == 1:
                change = (input("School Name: ")).title()
                update = ''' UPDATE education SET school = ? WHERE username = ?'''

            elif edit_option == 2:
                change = (input("Enter your Degree: ")).title()
                update = ''' UPDATE education SET degree = ? WHERE username = ?'''

            elif edit_option == 3:
                change = ui.integer("Full Years Attended to Date: ")
                update = ''' UPDATE education SET years = ? WHERE username = ?'''

            cursor.execute(update, [change, username])
            db.commit()

            print(ui.edit_education_menu)
            edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_education_menu)

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
        about = ui.mutli_line_string("Write Your About Section: ")

        cursor.execute(
            """
        INSERT INTO profiles (username, title, major, university, about) VALUES(?,?,?,?,?)""",
            (username, title, major, university, about),
            )
        db.commit()

        print("You Have Entered in profile: ", title)

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
        edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while(edit_option != 5):

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
                change = ui.mutli_line_string("Write Your About Section: ")
                update = ''' UPDATE profiles SET about = ? WHERE username = ?'''

            cursor.execute(update, [change, username])
            db.commit()

            print(ui.edit_profile_menu)
            edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

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
        print("editUserProfile: ", username)
        title = (ui.single_line_string("Enter your Title (E.g., Student): ")).title()
        employer = (ui.single_line_string("Enter your Employer: ")).title()
        started = ui.single_line_string("Enter Your Start Date: ")
        ended = ui.single_line_string("Enter Your End Date: ")
        location = (ui.single_line_string("Enter Location of Job: ")).title()
        description = ui.mutli_line_string("Enter Description: ")

        cursor.execute(
            """
        INSERT INTO jobs (username, title, employer, started, ended, location, description) VALUES(?,?,?,?,?,?,?)""",
            (username, title, employer, started, ended, location, description),
            )
        db.commit()

        print("You Have Entered in Jobs: ", title)

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
        edit_option = ui.integer_in_range("Enter which to edit: ", 1, 5, ui.edit_profile_menu)

        while(edit_option != 7):

            if edit_option == 1:
                change = title = (ui.single_line_string("Enter your Title (E.g., Student): ")).title()
                update = ''' UPDATE jobs SET title = ? WHERE username = ? AND title = ?'''

            elif edit_option == 2:
                change = employer = (ui.single_line_string("Enter your Employer: ")).title()
                update = ''' UPDATE jobs SET employer = ? WHERE username = ? AND title = ?'''

            elif edit_option == 3:
                change = ui.single_line_string("Enter Your Start Date: ")
                update = ''' UPDATE jobs SET started = ? WHERE username = ? AND title = ?'''

            if edit_option == 4:
                change = ui.single_line_string("Enter Your End Date: ")
                update = ''' UPDATE jobs SET ended = ? WHERE username = ? AND title = ?'''

            elif edit_option == 5:
                change = (ui.single_line_string("Enter Location of Job: ")).title()
                update = ''' UPDATE jobs SET location = ? WHERE username = ? AND title = ?'''

            elif edit_option == 6:
                change = ui.mutli_line_string("Enter Description: ")
                update = ''' UPDATE jobs SET description = ? WHERE username = ? AND title = ?'''

            cursor.execute(update, [change, username, jobTitle])
            db.commit()

            print(ui.edit_job_menu)
            edit_option = ui.integer_in_range("Enter which to edit: ", 1, 7, ui.edit_job_menu)
    
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

    choice = ui.integer_in_range("Select One of the Jobs to Edit by number: ", 1, len(number), "NULL")
    return (number[choice - 1][2])

def displayUser(username):
    displayUserProfile(username)
    displayUserEducation(username)
    displayUserJob(username)

def displayUserProfile(username):
    print("Display Profile: ", username)

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
        print("\n---------- Education ----------")
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


def emptyDatabase():
    db.commit()

    # enter SQL queries here
    cursor.execute("DELETE * FROM user")
    db.commit()

