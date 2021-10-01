import Login
import pytest

########################################## Testing for the Logged in Options


#####################################################
## Testing for Loggin in and viewing the Job Board ##
#####################################################

########################################## Test - Option 1

def test_1(capsys):
    input_values = [2, "Derryk", "9^rNeC232*", "Derryk", "Theberge", 1, "Derryk", "9^rNeC232*", 1, "no"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Enter Credentials to Login:

You Have Registered Derryk


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Existing Accounts:
  1: Derryk

- Enter Credentials to Login -


You have Logged In Derryk

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill


Welcome to the job posting page


                    Software Engineering Internship (SpaceX) -- Palo Alto, California
                    Minimum requirements
                    - Bachelor's degree in Computer Science/ Computer Engineering
                    - Experience in Jira
                    - Experience in Agile Environment
                    - Good experience in Java, C++, C
                    - Must have experience in Deep learning and Big data

                    Application Deadline 10/01/2021

                            Apply Now


Goodbye
"""
    assert err == ''

########################################## Test - Option 2

def test_2(capsys):
    input_values = [2, "John", "9^rNeC232*", "John", "Johnson", 1, "John", "9^rNeC232*", 2, "Derryk", "Theberge", 1, "no"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


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


Existing Accounts:
  1: Derryk
  2: John

- Enter Credentials to Login -


You have Logged In John

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill


They are a part of the InCollege System

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill


Welcome to the job posting page


                    Software Engineering Internship (SpaceX) -- Palo Alto, California
                    Minimum requirements
                    - Bachelor's degree in Computer Science/ Computer Engineering
                    - Experience in Jira
                    - Experience in Agile Environment
                    - Good experience in Java, C++, C
                    - Must have experience in Deep learning and Big data

                    Application Deadline 10/01/2021

                            Apply Now


Goodbye
"""
    assert err == ''


########################################## Test - Option 3

def test_3(capsys):
    input_values = [2, "Adelaide", "9^rNeC232*", "Adelaide", "Smith", 1, "Adelaide", "9^rNeC232*", 3, 1]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Enter Credentials to Login:

You Have Registered Adelaide


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Existing Accounts:
  1: Derryk
  2: John
  3: Adelaide

- Enter Credentials to Login -


You have Logged In Adelaide

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill

Pick a Skill to Learn More About
1. Communication Skills
2. Management Skills
3. Business Skills
4. Analytical Skills
5. Information Technology (IT) Skills
6. I Want to Return to the Menu

Under Construction

"""
    assert err == ''

########################################## Test - Option 4

def test_4(capsys):
    input_values = [2, "Mabel", "9^rNeC232*", "Mabel", "Smith", 1, "Mabel", "9^rNeC232*", 3, 6, "Yes", 1, "No"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""
----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Enter Credentials to Login:

You Have Registered Mabel


----- Success Story -----
 'When I was in college, I was actively looking for internships and inCollege helped me land with my dream job.
                  Now I'm flipping patties and making more money than my friends!'
                                                                                - Gelo Pikalov
----- Login Page -----
Please Select One of the Following Options

1. Login Using Existing InCollege Account
2. Create a New InCollege Account


Existing Accounts:
  1: Derryk
  2: John
  3: Adelaide
  4: Mabel

- Enter Credentials to Login -


You have Logged In Mabel

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill

Pick a Skill to Learn More About
1. Communication Skills
2. Management Skills
3. Business Skills
4. Analytical Skills
5. Information Technology (IT) Skills
6. I Want to Return to the Menu

Are You Sure You Want to Return?

Pick an Option:
  1. Search for a job/internship
  2. Find someone that you may know
  3. Learn a new skill


Welcome to the job posting page


                    Software Engineering Internship (SpaceX) -- Palo Alto, California
                    Minimum requirements
                    - Bachelor's degree in Computer Science/ Computer Engineering
                    - Experience in Jira
                    - Experience in Agile Environment
                    - Good experience in Java, C++, C
                    - Must have experience in Deep learning and Big data

                    Application Deadline 10/01/2021

                            Apply Now


Goodbye
"""
    assert err == ''


