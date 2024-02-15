import pytest
#Test case vode must be inside a method
#Test case method must be started with 'test_' 

a=101
actual_result = 'Testing'

#Decorator
@pytest.mark.TopPriority
@pytest.mark.skipif(a>100, reason="Skip as this functionality is not working, developer will fix it in new build")
def test_tc_001_Login_Logout_Testing():
    print('This is Top Priority')
    print('This is end of our test case code')

@pytest.mark.TopPriority
def test_tc_003_Login_Logout_Invalid_Credentials():
    print('This is Top Priority')
    print('This is end of testcase')
    assert actual_result == 'Hello', f'These 2 values must be same'


# Print statement output display on console: pytest -s 
# Verbose mode - display test cases name with status: pytest -v     