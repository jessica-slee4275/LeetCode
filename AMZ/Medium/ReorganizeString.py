"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""
 
Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        freq = Counter(s)
        
        # Create a max heap based on the frequency of characters
        max_heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(max_heap)
        
        # Variable to keep the previous character and its frequency
        prev_freq, prev_char = 0, ''
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            # If previous character exists, push it back into the heap
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            # Update the previous character and frequency
            prev_freq, prev_char = freq + 1, char
        
        rearranged_string = ''.join(result)
        return rearranged_string if len(rearranged_string) == len(s) else ""
