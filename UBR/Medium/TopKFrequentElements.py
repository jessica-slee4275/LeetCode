"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_items = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        # arrange by value x[1]
        return [item[0] for item in sorted_items][:k]
