class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a

OUTPUT:
n=2
O/p:
1
