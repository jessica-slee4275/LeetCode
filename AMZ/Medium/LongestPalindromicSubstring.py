"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        
        max_length = 0  
        start_index = 0  
        
        for i in range(len(s)):
            l, r = i, i
            # odd len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    start_index = l
                print(f'A i:{i}, l:{l}, r:{r}, len:{r-l+1}, max_length:{max_length}, {s[l:r+1]}')
                l -= 1
                r += 1
            
            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    start_index = l
                print(f'B i:{i}, l:{l}, r:{r}, len:{r-l+1}, max_length:{max_length}, {s[l:r+1]}')
                l -= 1
                r += 1
                
        return s[start_index:start_index + max_length]
