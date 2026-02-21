class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=[]
        n=[]
        primes=[]
        count=0
        for i in range(left,right+1):
            m=bin(i)[2:]
            c.append(str(m))
        for j in c:
            count+=j.count("1")
            n.append(count)
            count=0
        for i in n:
            if(i>1):
                for j in range(2,int(i**0.5)+1):
                    if(i%j==0):
                        break
                else:
                    primes.append(i)
        return len(primes)
print(Solution().countPrimeSetBits(6,10))        

output:
Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
