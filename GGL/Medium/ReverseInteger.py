"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
-2**31 <= x <= 2**31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if x < 0:
            reversed_x = int('-'+((str(x)[1:])[::-1]))
        else:
            reversed_x = int(str(x)[::-1])
        
        if INT_MAX < reversed_x or INT_MIN > reversed_x:
            return 0
        else:
            return reversed_x
        
