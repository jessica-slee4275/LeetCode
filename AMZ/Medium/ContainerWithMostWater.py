"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [2,3,4,5,18,17,6]
Output: 17
"""

class Solution:
    """
    height = [2,3,4,5,18,17,6]
    output = 17
    """
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height)-1 

        while i < j:
            res = max(res, (j-i)*min(height[i], height[j]))
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
              
        # Time limit reached
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         # print(height[i], height[j], min(height[i], height[j])*(j-i)) 
        #         res = max(min(height[i], height[j])*(j-i), res)
        return res
