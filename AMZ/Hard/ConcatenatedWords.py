"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:

1 <= words.length <= 10*4
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 10*5
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words_set and (suffix in words_set or dfs(suffix)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False
        
        for word in words:
            if word and dfs(word):
                res.append(word)
        return res
