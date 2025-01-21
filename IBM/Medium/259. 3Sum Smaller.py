"""
Given an array of n integers nums and an integer target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
 
Constraints:
n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        cnt = 0
        for i in range(len_nums-2):
            l, r = i+1, len_nums-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total < target:
                    # move l to the right, add all combinations
                    cnt += (r-l)
                    l += 1
                else:
                    r -= 1
        return cnt
