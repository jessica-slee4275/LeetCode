"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk_a, stk_b = [], []
        for a in s:
            if a == '#':
                if len(stk_a)!=0: stk_a.pop()
            else: stk_a.append(a)
        for b in t:
            if b == '#': 
                if len(stk_b)!=0: stk_b.pop()
            else: stk_b.append(b)
        return ''.join(stk_a) == ''.join(stk_b)
