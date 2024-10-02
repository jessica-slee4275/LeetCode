"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:
1 <= nums.length <= 5 * 10**5
-2**31 <= nums[i] <= 2**31 - 1
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if len(list(set(nums))) < 3: return False
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         if nums[i] < nums[j]:
        #             for k in range(j+1, len(nums)):
        #                 if nums[i] < nums[j] < nums[k]:
        #                     return True
        # return False

        n = len(nums)
        if n < 3:
            return False

        # Initialize variables to track the minimum first and second elements
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # Found an increasing triplet
                return True

        return False
