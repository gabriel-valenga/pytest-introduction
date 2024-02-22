import pytest
#Test case vode must be inside a method
#Test case method must be started with 'test_' 

# @pytest.fixture(scope='module') #to execute fixture code only before the first test case and after the last test case in this file
@pytest.fixture()
def fixture_code():
    print('This is our fixture code, will be executed before the test case')
    yield 
    print('This is our fixture code, will be executed after the test case')

#Decorator
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_Login_Logout_Testing(fixture_code):
    print('This is Smoke')
    print('This is end of our test case code')

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_Login_Logout_Invalid_Credentials(fixture_code):
    print('This is Sanity')
    print('This is end of testcase')


# Print statement output display on console: pytest -s 
# Verbose mode - display test cases name with status: pytest -v     