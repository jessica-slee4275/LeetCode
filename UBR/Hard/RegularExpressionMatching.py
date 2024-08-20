"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
    """
    s = "abcd"
    p = "a***abc"
    false

    s = "abc"
    p = "a***abc"
    true
    """
    def isMatch(self, s: str, p: str) -> bool:
        # if '*' not in p and '.' not in p :
        #     return s == p

        if '**' in p:
            if s in p.replace('*',''):
                return True
            else:
                return False
            
        x = re.search(rf'{p}', s)
        if x:
            return x.group() == s
        return False
            
