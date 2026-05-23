class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        b=s+s
        if(len(goal)==len(s) and goal in b):
            return True
        else:
            return False


OUTPUT:
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
