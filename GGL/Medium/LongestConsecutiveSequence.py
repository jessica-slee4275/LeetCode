"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Input nums = [9,1,4,7,3,-1,0,5,8,-1,6]
Output 7

Input nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
Output 4

Constraints:
0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        start = 0
        res = 0
        # print(nums)
        for i in range(len(nums)-1):
            if nums[i]+1 < nums[i+1]:
                # print('>> ', start, i, nums[start:i+1])
                res = max(i+1-start, res)
                start = i+1
            i += 1
        if res != 0:
            res = max(i+1-start, res)
        return len(nums) if res == 0 else res
