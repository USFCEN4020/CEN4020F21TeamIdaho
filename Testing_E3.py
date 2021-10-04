import Login
import pytest


#####################################################
## Testing for two groups of Incollege navigation links, "Useful Links" & "Incollege Important Links" ##
#####################################################

########################################## Test1 - Test private policy is selected & guest controls is provided ##

def test_1(capsys):
    input_values = [2, "John", "9^rNeC232*", "John", "Johnson", 1, "John", "9^rNeC232*", 4, 5, 1]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Enter Credentials to Login:

You Have Registered John


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Existing Accounts:
  1: John

- Enter Credentials to Login -


You have Logged In John

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill
  4. InCollege Important Links
  5. Useful Links
Please choice one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Copyright Policy
8. Brand Policy
9. Languages

We take privacy very seriously. We promise to not share your private information to any third-party. We use maximum security to protect your information.
You also have reached the Guest Controls, where you
You can choose which ones to turn off.
1. InCollege Email
2. SMS
3. Targeted Advertising
4. None of them, return back to menu


"""
    assert err == ''

########################################## Test2 - Test all options in "Useful Links" before login and Test Sign Up feature ##

def test_2(capsys):
    input_values = [4, 1, 2, 3, 4, 5, 6, 7, 1, "Ayachi", "_NwpR-F8!3#", "Xiaohu", "Sun", 4, 1, 1, "Ayachi", "no"]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

We're here to help
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

In College Pressroom: Stay on top of the latest news, updates, and reports
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Enter Credentials to Login:

You Have Registered Ayachi


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Enter Credentials to Login:
An Account of that username exists
"""
    assert err == ''

########################################## Test3 - Tests Incollege Important Links and Copyright Notice ##

def test_3(capsys):
    input_values = [2, "Abby", "9^rNeC232*", "Abby", "Smith", 1, "Abby", "9^rNeC232*", 4, 1]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Enter Credentials to Login:

You Have Registered Abby


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Existing Accounts:
  1: John
  2: Ayachi
  3: Abby

- Enter Credentials to Login -


You have Logged In Abby

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill
  4. InCollege Important Links
  5. Useful Links
Please choice one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Copyright Policy
8. Brand Policy
9. Languages

This faux application for Walmart LinkedIn is protected by Copyright Laws. Reproduction of this code without permission is prohibited you baka

"""
    assert err == ''

########################################## Test4 - Test useful links & incollege important links before user signs in ##

def test_4(capsys):
    input_values = [4, 2, 3, 4, 1, 8, 5]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    #with pytest.raises(SystemExit):
    Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
Under construction
Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
Under construction
Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
Under construction
Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Please choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
"""
    assert err == ''

########################################## Test5 - There's no language option before user login and Copyright Notice is available to access ##

def test_5(capsys):
    input_values = [3, 7]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    #with pytest.raises(SystemExit):
    Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Please choose one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Coyright Policy
8. Brand Policy
9. Return to the main menu

Team Idaho respoects the intellectual property rights of others and expects the same for the users using this application.
"""
    assert err == ''


########################################## Test6 - Test language option on nCollege Important Links after login  ##

def test_6(capsys):
    input_values = [1, "Ayachi", "_NwpR-F8!3#", 4, 9, 2, 4, 9, 1, 4, 1]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links


Existing Accounts:
  1: John
  2: Ayachi
  3: Abby

- Enter Credentials to Login -


You have Logged In Ayachi

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill
  4. InCollege Important Links
  5. Useful Links
Please choice one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Copyright Policy
8. Brand Policy
9. Languages

Choose a language, English or Spanish?

Language changed to Spanish
Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill
  4. InCollege Important Links
  5. Useful Links
Please choice one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Copyright Policy
8. Brand Policy
9. Languages

Choose a language, English or Spanish?

Language changed to English
Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill
  4. InCollege Important Links
  5. Useful Links
Please choice one to learn more about
1. Copyright Notice
2. About
3. Accessibility
4. User Agreement
5. Privacy Policy
6. Cookie Policy
7. Copyright Policy
8. Brand Policy
9. Languages

This faux application for Walmart LinkedIn is protected by Copyright Laws. Reproduction of this code without permission is prohibited you baka

"""
    assert err == ''