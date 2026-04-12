class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen = set()
        for ch in s:
            if ch in seen:
                count += 1
                seen = set()
            seen.add(ch)
        return count    

OUTPUT:
Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
