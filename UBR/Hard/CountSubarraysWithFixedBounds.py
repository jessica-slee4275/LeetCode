"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 
Constraints:
2 <= nums.length <= 10**5
1 <= nums[i], minK, maxK <= 10**6
"""
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        # count subarr having specific range
        # left_idx: Leftmost index
        # right_idx: Rightnost index
        # bad_idx: Leftmost invalid index
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not minK <= num <= maxK:
                bad_idx = i
            if num == minK:
                left_idx = i
            if num == maxK:
                right_idx = i

            # print(num, (left_idx, right_idx), bad_idx, res, max(0, min(left_idx, right_idx) - bad_idx))
            res += max(0, min(left_idx, right_idx) - bad_idx) 

        # Time Limit Exceeded
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         subarr = nums[i:j+1]
        #         if min(subarr) == minK and max(subarr) == maxK:
        #             res += 1
        return res

