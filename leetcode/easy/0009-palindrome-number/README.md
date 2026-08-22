# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 221 ms (beats 5.54%)  
**Memory:** 12.3 MB (beats 90.52%)  
**Submitted:** 2026-08-22T17:30:24.644Z  

```py
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

```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)