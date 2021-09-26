import Login

##########################################
## Testing for account creation testing ##
##########################################

########################################## Test - Account creation for one account, with valid paassword


## PASSWORD TESTS

# Criteria 1 - >= 8 Characters
# Criteria 2 - <= 12 Characters
# Criteria 3 - Contain digit
# Criteria 4 - Contain Upper case letter
# Criteria 5 - Special Character


##########################################
## Testing for breaking only 1 Criteria ##
##########################################

########################################## Test - Less than 8 characters

def test_1(capsys):
    input_values = [2, "Derryk", "9^rNeC*"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input
 
    Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""----- Login Page -----
Please select one of the following options

1. Login using existing InCollege account
2. Create a new InCollege account
    

- Enter Credentials to Login -
Password must be 8 - 12 characters long 

"""
    assert err == ''


########################################## Test - More than 12 Characters

def test_2(capsys):
    input_values = [2, "Derryk", "sLwjt^#XNe5dU"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input
 
    Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""----- Login Page -----
Please select one of the following options

1. Login using existing InCollege account
2. Create a new InCollege account
    

- Enter Credentials to Login -
Password must be 8 - 12 characters long 

"""
    assert err == ''


########################################## Test - No Capital Letters

def test_3(capsys):
    input_values = [2, "Derryk", "jov*o7*^5j%"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input
 
    Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""----- Login Page -----
Please select one of the following options

1. Login using existing InCollege account
2. Create a new InCollege account
    

- Enter Credentials to Login -
Make sure that the password has a capital letter in it 

"""
    assert err == ''

########################################## Test - No Digits

def test_4(capsys):
    input_values = [2, "Derryk", "*YqSPy%pghy"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input
 
    Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""----- Login Page -----
Please select one of the following options

1. Login using existing InCollege account
2. Create a new InCollege account
    

- Enter Credentials to Login -
Make sure your password has a digit in it 

"""
    assert err == ''

########################################## Test - No Non-Alpha Characters

def test_5(capsys):
    input_values = [2, "Derryk", "W2KdRmtQWeT"]
 
    def mock_input(s):
        return input_values.pop(0)
    Login.input = mock_input
 
    Login.main()
 
    out, err = capsys.readouterr()
 
    assert out =="""----- Login Page -----
Please select one of the following options

1. Login using existing InCollege account
2. Create a new InCollege account
    

- Enter Credentials to Login -
Make sure that the password has a special letter in it 

"""
    assert err == ''
