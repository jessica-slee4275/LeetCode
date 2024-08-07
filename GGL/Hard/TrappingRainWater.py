"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 10**4
0 <= height[i] <= 10**5
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1

        max_left = height[l]
        max_right = height[r]

        water = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                # print('l', l, r, max_left, water)
            else:
                r -= 1
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                # print('r', l , r, max_right, water)

        return water
        
