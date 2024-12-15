"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10**4
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for first_index in range(0, len(nums)-1):
        #     for second_index in range(first_index+1, len(nums)):
        #         if target == nums[first_index] + nums[second_index]:
        #             return [first_index, second_index]
        # return []
        numMap = {}
        for i in range(len(nums)):
            t = target-nums[i]
            if t in numMap:
                return [numMap[t], i]
            numMap[nums[i]] = i
        return []
