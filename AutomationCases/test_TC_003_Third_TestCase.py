import pytest
#Test case vode must be inside a method
#Test case method must be started with 'test_' 

#Decorator
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_Login_Logout_Testing():
    print('This is Smoke')
    print('This is end of our test case code')

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_Login_Logout_Invalid_Credentials():
    print('This is Sanity')
    print('This is end of testcase')


# Print statement output display on console: pytest -s 
# Verbose mode - display test cases name with status: pytest -v     