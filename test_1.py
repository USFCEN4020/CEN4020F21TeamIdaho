import login_main
import pytest

def test_1(capsys):
    input_values = ["2", "John", "9^rNeC232*", "John", "Johnson", "Standard","5"]

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
    input_values = ["2", "Derryk", "9^rNeC232*", "Derryk", "Theberge", "Standard", "5",]

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

You Have Registered Derryk

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

def test_3(capsys):
    input_values = ["2", "Christopher", "9^rNeC232*", "Christopher", "Close", "Plus", "5",]

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

You Have Registered Christopher

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

def test_4(capsys):
    input_values = ["1", "John", "9^rNeC232*", "20", "1", "Derryk", "3", "21"]

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

Existing Accounts:
  1: John
  2: Derryk
  3: Christopher

1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit


1. Standard Student Messaging
2. Plus Student Messaging
3. Go back

I'm sorry, you are not friends with that person.

1. Standard Student Messaging
2. Plus Student Messaging
3. Go back


1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit

Goodbye, Have a Nice Day !
"""
    assert err == ''


def test_5(capsys):
    input_values = ["1", "Christopher", "9^rNeC232*", "20", "2", "Derryk", "Hello Derryk!", "3", "21"]

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

Existing Accounts:
  1: John
  2: Derryk
  3: Christopher

1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit


1. Standard Student Messaging
2. Plus Student Messaging
3. Go back

These are the users that you can message:
      John
      Derryk
You Have sent the message to Derryk

1. Standard Student Messaging
2. Plus Student Messaging
3. Go back


1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit

Goodbye, Have a Nice Day !
"""
    assert err == ''

def test_6(capsys):
    input_values = ["1", "Derryk", "9^rNeC232*", "1", "3", "5"]

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

Existing Accounts:
  1: John
  2: Derryk
  3: Christopher
You have received a message in your inbox.
NOTIFICATION: You have received a message from Christopher
Message:  Hello Derryk!
You have removed the message from your inbox

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
    input_values = ["1", "Christopher", "9^rNeC232*", "20", "2", "Derryk", "Hello Derryk!", "3", "21"]

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

Existing Accounts:
  1: John
  2: Derryk
  3: Christopher

1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit


1. Standard Student Messaging
2. Plus Student Messaging
3. Go back

These are the users that you can message:
      John
      Derryk
You Have sent the message to Derryk

1. Standard Student Messaging
2. Plus Student Messaging
3. Go back


1. Search for a Job / Internship
2. Apply for a Job
3. List of Applied / Not-Applied Jobs
4. List of Saved Jobs / Unsave a Job
5. Find Someone That You May Know
6. Learn a New Skill
7. InCollege Important Links
8. Useful Links
9. Create Your User Profile
10. Create Education
11. Create a Job
12. Edit Your User Profile
13. Edit Your Education
14. Edit Jobs
15. Delete Jobs
16. Display a User Profile
17. Send a Friend Request
18. List Pending Requests
19. Show My Network
20. Send a message
21. Exit

Goodbye, Have a Nice Day !
"""
    assert err == ''

def test_8(capsys):
    input_values = ["1", "Derryk", "9^rNeC232*", "1", "2", "Christopher", "My life is a dumpster fire", "5"]

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

Existing Accounts:
  1: John
  2: Derryk
  3: Christopher
You have received a message in your inbox.
NOTIFICATION: You have received a message from Christopher
Message:  Hello Derryk!
You Have sent the message to Christopher

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
