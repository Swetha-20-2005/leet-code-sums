n=int(input())
a=[]
count=0
for i in range(0,n):
    b=input()
    a.append(b)
c="".join(a)
m=sorted(c)
for i in sorted(set(m)):
    count=m.count(i)
    print(i,count)

OUTPUT:
i/p:
2
hello
good
o/p:
d 1
e 1
g 1
h 1
l 2
o 3
