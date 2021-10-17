import login_main
import pytest

def test_1(capsys):
    input_values = ["2", "John", "9^rNeC232*", "John", "Johnson", "5",]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    with pytest.raises(SystemExit):
        login_main.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!
                                                                                - Gelo Pikalov
--------------- Login Page ---------------
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
5. Exit

You Have Registered John

----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!
                                                                                - Gelo Pikalov
--------------- Login Page ---------------
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
5. Exit

"""
    assert err == ''

def test_2(capsys):
    input_values = ["1st year Computer Science student", "Computer Science", "USF", "A computer science student looking for more job opportunities!", ""]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    #with pytest.raises(SystemExit):
    login_main.createUserProfile("John")

    out, err = capsys.readouterr()

    assert out == """Your profile has been created.
"""
    assert err == ''

def test_3(capsys):
    input_values = ["USF", "Computer Science", "4", ""]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.createEducation("John")

    out, err = capsys.readouterr()

    assert out == """Your education section has been created.
"""
    assert err == ''


def test_4(capsys):
    input_values = ["Student", "JPMorgan", "4/12/21", "8/12/21", "Tampa", "Working with JPMorgan", ""]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.createJob("John")

    out, err = capsys.readouterr()

    assert out == """Your job has been created.
"""
    assert err == ''

def test_5(capsys):
    input_values = []

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.displayUser("John", "Karen")

    out, err = capsys.readouterr()

    assert out == """You are not friends with them to view their profile
"""
    assert err == ''

##New test cases
def test_6(capsys):
    input_values = ["2", "Karen", "9^rNeC232*", "Karen", "Jones", "5",]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    with pytest.raises(SystemExit):
        login_main.main()

    out, err = capsys.readouterr()

    assert out == """
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!
                                                                                - Gelo Pikalov
--------------- Login Page ---------------
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
5. Exit

You Have Registered Karen

----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!
                                                                                - Gelo Pikalov
--------------- Login Page ---------------
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account
3. InCollege Important Links
4. Useful Links
5. Exit

"""
    assert err == ''

def test_7(capsys):
    input_values = ["3rd year Computer Science student", "Computer Science", "USF", "A computer science student looking for more job opportunities!", ""]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    #with pytest.raises(SystemExit):
    login_main.createUserProfile("Karen")

    out, err = capsys.readouterr()

    assert out == """Your profile has been created.
"""
    assert err == ''

def test_8(capsys):
    input_values = ["USF", "Computer Science", "3", ""]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.createEducation("Karen")

    out, err = capsys.readouterr()

    assert out == """Your education section has been created.
"""
    assert err == ''

##Send Friend Request
def test_9(capsys):
    input_values = []

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.friend_request("John", "Karen")

    out, err = capsys.readouterr()

    assert out == """You Have sent friend request to Karen
"""
    assert err == ''

##Execute Friend Request
def test_10(capsys):
    input_values = ["1"]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.exec_friend_request("Karen")

    out, err = capsys.readouterr()

    assert out == """
Would you like to accept friend request from John
You have accepted friend request from, John
"""
    assert err == ''

#Displays User
def test_11(capsys):
    input_values = []

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.displayUser("John", "Karen")

    out, err = capsys.readouterr()

    assert out == """
---------- You are viewing  Karen Jones 's profile ----------
Title:  3Rd Year Computer Science Student
Major:  Computer Science
University:  Usf
About: :  A computer science student looking for more job opportunities!


---------- Education ----------
School:  Usf
Degree:  Computer Science
Years Attended:  3
"""
##List of Friends
def test_12(capsys):
    input_values = ["No"]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    # with pytest.raises(SystemExit):
    login_main.listFriends("John")
    out, err = capsys.readouterr()

    assert out == """Your Friends:
      Karen
"""
    assert err == ''

