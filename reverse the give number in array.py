a=int(input())
b=int(input())
q=list(map(int,input().split()))
n=[]
for i in q[:b]:
    n.append(i)
    q.remove(i)
m=n[::-1]
c=m+q
print(*c)

Example:
5
4
1 2 3 4 5
OUTPUT:
4 3 2 1 5
