"""
You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:
1 <= pivot < n
nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.

Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.

 

Example 1:
Input: nums = [2,-1,2], k = 3
Output: 1
Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
There is one way to partition the array:
- For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
Example 2:

Input: nums = [0,0,0], k = 1
Output: 2
Explanation: The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
Example 3:

Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
Output: 4
Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
There are four ways to partition the array.
 

Constraints:

n == nums.length
2 <= n <= 10**5
-10**5 <= k, nums[i] <= 10**5
"""
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        # prefix = [0]
        # loc = defaultdict(list)
        # for i, x in enumerate(nums):
        #     prefix.append(prefix[-1] + x)
        #     if i < len(nums)-1: loc[prefix[-1]].append(i)
        # print(loc)
        # res = 0
        # # Input nums = [0,0,0], k = 1
        # if prefix[-1] % 2 == 0: 
        #     res = len(loc[prefix[-1]//2])
        # total = prefix[-1]
        # for i, x in enumerate(nums):
        #     cnt = 0
        #     diff = k - x
        #     target = total + diff

        #     if target % 2 == 0:
        #         target //= 2
        #         cnt += bisect_left(loc[target], i)
        #         cnt += len(loc[target-diff]) - bisect_left(loc[target-diff], i)
        #     res = max(res, cnt)
        # print('>>',res)


        l, r = 0, sum(nums)
        d = defaultdict(list)
        prev = nums[0]
        n = len(nums)
        res = 0
        for i in range(1, n):
            l += prev
            r -= prev
            if (l==r): res += 1
            d[r-l].append(i)
            # print(l, r, r-l, i)
            prev = nums[i]
        print(d)
        for i in range(n):
            diff = k-nums[i]
            left = right = 0
            if diff in d:
                right = len(d[diff])-bisect_left(d[diff], i+1)
            if d[-diff] and d[-diff][0] <= i:
                left = bisect_right(d[-diff], i)
            res = max(res, left+right)
        return res

