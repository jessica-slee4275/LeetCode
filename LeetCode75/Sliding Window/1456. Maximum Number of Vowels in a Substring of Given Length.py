"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 
Constraints:
1 <= s.length <= 10**5
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Time Limit Exceeded
        # res = 0
        # for i in range(len(s)-k+1):
        #     if s[i] or s[i+k] in 'aeiou':
        #         res = max(sum(1 for char in s[i:i+k] if char in 'aeiou'), res)
        # return res

        vowels = 'aeiou'
        cnt = ans = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            cnt += (s[i] in vowels)-(s[i-k] in vowels)
            ans = max(cnt, ans)
        return ans
