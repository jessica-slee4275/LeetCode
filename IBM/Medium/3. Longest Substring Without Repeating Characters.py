"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, max_length = 0, 0
        char_index_map = dict()
        for r in range(n): # current check char
            if s[r] in char_index_map: # if have duplicate char
                l = max(l, char_index_map[s[r]]+1) # max: left always goes to right
            max_length = max(max_length, r-l+1)
            char_index_map[s[r]] = r
            print(char_index_map, l, r, s[l:r+1], max_length)
        return max_length
