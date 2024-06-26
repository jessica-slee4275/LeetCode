"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:
0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
nums is a non-decreasing array.
-10**9 <= target <= 10**9
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first_index = nums.index(target)
            last_index = first_index
            temp_nums = nums[first_index+1:]
            
            while target in temp_nums:
                last_index = last_index+nums[last_index:].index(target)+1
                temp_nums = nums[last_index+1:]
            return [first_index, last_index]
        return [-1,-1]
