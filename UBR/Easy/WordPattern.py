"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s_split = s.split()

        if len(pattern) != len(s_split):
            return False

        for p, word in zip(pattern, s_split):
            if p in d and d[p] != word:
                return False
            d[p] = word

        return True

        # d = defaultdict()
        # s = s.split(' ')
        
        # for p in pattern:
        #     if p not in d.keys():
        #         d[p] = ""

        # for ss in s:
        #     Found = False
        #     for k, v in d.items():
        #         if v == ss:
        #             Found = True
        #             break
        #     if not Found:
        #         for key, value in d.items():
        #             if d[key] == "":
        #                 d[key] = ss
        #                 break
            
        # lpattern = []
        # for p in pattern:
        #     lpattern.append(d[p])
        # return True if lpattern == s else False
        
