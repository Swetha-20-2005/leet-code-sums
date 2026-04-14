import queue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = queue.PriorityQueue()
        for i in nums:
            q.put(i)
            if q.qsize() > k:
                q.get()
        while not q.empty():
            return q.get()
            break


OUTPUT:
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
