class Solution(object):
    def isPalindrome(self, x):
        print("Input:", x)

        # Negative numbers are not palindromes
        if x < 0:
            print("Output: false")
            return False

        # Numbers ending in 0 cannot be palindrome (except 0)
        if x % 10 == 0 and x != 0:
            print("false")
            return False

        rev = 0

        # Reverse only half the number
        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10


        result = (x == rev) or (x == rev // 10)

        print("result")
        return result
