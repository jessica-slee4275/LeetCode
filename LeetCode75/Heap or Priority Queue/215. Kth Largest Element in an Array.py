"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time Limit Exceeded
        # while k > 1 :
        #     nums.pop(nums.index(max(nums)))
        #     k -= 1
        # return max(nums)
        
        nums = [-num for num in nums]
        heapq.heapify(nums) # not perfectly sorting, good to find minimum value
        # Remove the largest elements k-1 times
        for _ in range(k-1):
            heapq.heappop(nums)
                  
        # The remaining top element is the k-th largest
        return heapq.heappop(nums)*-1
