"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 10**4
s and t consist only of lowercase English letters.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        T = O(N)
        S = O(1)
        """
        sp = tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)

        # doesn't work for s = "aaaaaa", t = "bbaaaa"
        # t = list(t)
        # ans = []
        # for c in s:
        #     if c not in t:
        #         return False
        #     ans.append(t.index(c))
        # print(ans)
        # return ans == sorted(ans) 
