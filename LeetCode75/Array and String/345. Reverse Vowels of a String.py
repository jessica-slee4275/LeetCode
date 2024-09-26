"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10**5
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 40 ms
        # m = 'aeiouAEIOU'
        # vowels = [ch for ch in s if ch in m]    
        # vowels = vowels[::-1]
        # index = 0
        # res = list(s)
        # for i, ch in enumerate(s):
        #     if ch in m:
        #         res[i] = vowels[index]
        #         index += 1

        # return ''.join(res)

        # 49 ms
        s = list(s)
        l, r = 0, len(s)-1
        m = 'aeiouAEIOU'
        while l < r:
            if s[l] in m and s[r] in m:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in m: l += 1
            elif s[r] not in m: r -= 1
        return ''.join(s)
        
