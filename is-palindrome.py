# is_palindrome("radar")  # Should return True
def is_palindrome(string):
    palindrome = ''.join(i for i in list(string)[::-1])
    return False if palindrome != string else True

is_palindrome("radar") #It returns "True"