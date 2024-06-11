"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        negative = []
        positive = []
        zero = []

        for num in nums:
            if num > 0: positive.append(num)
            elif num < 0: negative.append(num)
            else: zero.append(num)

        set_negative, set_positive = set(negative), set(positive)
      
        if zero:
            for num in set_positive:
                if -1*num in set_negative:
                    res.add((-1*num, 0, num))
            if len(zero) >= 3:
                res.add((0,0,0))

        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = -1*(negative[i]+negative[j])
                if target in set_positive:
                    res.add(tuple(sorted([negative[i], negative[j], target])))
        
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = -1*(positive[i]+positive[j])
                if target in set_negative:
                    res.add(tuple(sorted([positive[i], positive[j], target])))
                    # tuple? for unhashable type: 'list'
      
        return res
