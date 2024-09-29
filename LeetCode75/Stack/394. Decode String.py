"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
import re
class Solution:
    def decodeString(self, s: str) -> str:
        # T : O(N^2) # re.search within the while loop
        # S : O(N) # extra space for variables (has_match, match) and the temporary string s during replacements.
        # has_match = True

        # while has_match:
        #     match = re.search(r'(\d+)\[(\w+)\]', s)
        #     if match:
        #         s = s.replace(match.group(), int(match.group(1))*match.group(2))
        #     has_match = re.search(r'(\d+)\[(\w+)\]', s)
        # return s

        # T : O(N) # for loop
        # S : O(N) # stk (curStr, curNum are temp) 
        stk = []
        curStr = ''
        curNum = 0
        for c in s:
            if c == '[':
                stk.append(curStr)
                stk.append(curNum)
                curStr = ''
                curNum = 0
            elif c == ']':
                num = stk.pop()
                prevStr = stk.pop()
                curStr = prevStr + num*curStr
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curStr += c
        return curStr
