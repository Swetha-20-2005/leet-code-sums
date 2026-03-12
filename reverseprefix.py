class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]

OUTPUT:
"abcd" k=2
O/P
"bacd"
