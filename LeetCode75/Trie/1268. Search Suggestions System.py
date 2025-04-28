"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

Constraints:
1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * (10**4)
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.words) < 3: node.words.append(word)
    def search(self, prefix:str) -> list:
        node = self.root
        res = []
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
                res.append(node.words)
            else:
                while len(res) < len(prefix): res.append([])
                break
        return res
# Trie 63ms  
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        return trie.search(searchWord)      
      
# binary search 5ms   
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         res, prefix = [], ""
      
#         for ch in searchWord:
#             prefix += ch
#             i = bisect.bisect_left(products, prefix)
#             suggestions = []
#             for j in range(i, min(i + 3, len(products))):
#                 if products[j].startswith(prefix):
#                     suggestions.append(products[j])
#                 else: break
#             res.append(suggestions)
#         return res
      
# 310ms   
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
#         res = []
#         products.sort()
#         for i in range(1, len(searchWord)+1):
#             r = []
#             for product in products:
#                 if product.startswith(searchWord[:i]): r.append(product)
#                 if len(r) == 3: break
#             res.append(r)
#         return res

  
