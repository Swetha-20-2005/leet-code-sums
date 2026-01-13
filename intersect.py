from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)   # count ah control pannum
        return res

print(Solution().intersect([1,2,2,1],[2,2]))
