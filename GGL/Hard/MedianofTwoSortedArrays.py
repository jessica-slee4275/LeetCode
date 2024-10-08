"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1 + nums2)
        # res = sorted(nums1+nums2)
        # len_res = len(res)
        # if len_res == 1: return res[0]/1
        
        # if len_res % 2 == 1:
        #     return res[len_res//2]
        # else:
        #     return (res[len_res//2-1]+res[len_res//2])/2
