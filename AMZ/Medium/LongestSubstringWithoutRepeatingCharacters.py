"""
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
 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        char_index_map = dict()
        left = 0

        for right in range(n): # current check char
            if s[right] in char_index_map: # if have duplicate char
                left = max(left, char_index_map[s[right]] + 1) # max: left always goes to right
            max_length = max(max_length, right - left + 1)
            char_index_map[s[right]] = right
            print(char_index_map, left, right, s[left:right+1], max_length)

        return max_length
