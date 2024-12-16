"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:
Input: nums = [1,1,1]
Output: 0
 
Constraints:
n == nums.length
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
The answer is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)  
        total_sum = sum(nums)   
        return total_sum - min_num * len(nums)
        
        # Time Limit Exceeded
        # cnt = 0
        # while len(set(nums)) > 1:
        #     nums = sorted(nums)
        #     for i in range(len(nums)-1):
        #         nums[i] += 1
        #     cnt += 1
        # return cnt
        
