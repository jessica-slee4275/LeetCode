"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:
-10**5 <= num <= 10**5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10**4 calls will be made to addNum and findMedian.
"""

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num) #  maxheap, so -1 * num
        heappush(self.large, -self.small[0]) #  minheap
        heappop(self.small)
        # print('>', self.small, self.large)
        if len(self.small) < len(self.large):
            heappush(self.small, -self.large[0])
            heappop(self.large)
        # print('>>', self.small, self.large)

    def findMedian(self) -> float:
        print(self.small, self.large)
        if len(self.small) > len(self.large):
            return -self.small[0]   
        else:
            return (self.large[0]-self.small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
