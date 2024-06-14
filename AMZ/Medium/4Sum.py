"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.findNSum(nums, target, 4, [], res)
        return res

    def findNSum(self, nums, target, N, prefix, result):
        len_nums = len(nums)
        if N == 2:
            l, r = 0, len_nums-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    print(f'>>>> result.append{prefix+[nums[l], nums[r]]}')
                    result.append(prefix+[nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(len_nums-N+1): # +1 is for nums=[0,0,0,0], target=0
                print(f'len_nums:{len_nums}, N:{N}, target:{target}, N*nums[{i}]:{N*nums[i]}, N*nums[-1]:{N*nums[-1]}')
                if target < N*nums[i] or target > N*nums[-1]:
                    break
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    # print(f'i:{i}, nums[{i}]:{nums[i]}, nums[{i-1}]:{nums[i-1]}, nums[{i+1}:]:{nums[i+1:]}, target-nums[{i}]={target-nums[i]}, {prefix}+[{nums[i]}]={prefix+[nums[i]]}')
                    print(f'>> findNSum nums[{i+1}:]:{nums[i+1:]}, target-nums[{i}]:{target-nums[i]}, N: {N-1}, {prefix}+[{nums[i]}]={prefix+[nums[i]]}')
                    self.findNSum(nums[i+1:], target-nums[i], N-1, prefix+[nums[i]], result)
        return result

        
