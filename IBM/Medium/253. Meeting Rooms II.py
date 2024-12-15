"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:
1 <= intervals.length <= 10**4
0 <= starti < endi <= 10**6
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        sorted_intervals = sorted(intervals)

        for i in sorted_intervals:
            if h == [] or h[0] > i[0]:
                heapq.heappush(h, i[1])
            else:
                heapq.heapreplace(h, i[1])
        
        return len(h)
