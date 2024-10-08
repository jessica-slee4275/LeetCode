"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:
1 <= s.length <= 10**5
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_count = {}
        max_count = 0
        max_len = 0
        left = 0

        for right in range(n):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            # char_count.get(s[right], 0)  -> if the key doesn't exist, set its value to 0
            max_count = max(max_count, char_count[s[right]])
            if (right-left+1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
