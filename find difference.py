class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n=[]
        m=[]
        for i in nums1:
            if(i not in nums2):
                if i not in n:
                    n.append(i)
        for i in nums2:
            if(i not in nums1):
                if i not in m:
                    m.append(i)
        return [n,m]
print(Solution().findDifference([1,2,3],[2,4,6]))          
