a=[1,1,5,4,7,2]
tar=9
for i in a[::-1]:
    for j in a[::-1]:
        if (i+j==tar):
            print(i,j)
    break
            
           
ANOTHER METHOD

a=[1,1,5,4,7,2]
tar=9
for i in range(len(a)-1,-1,-1):
    for j in range(len(a)-1,-1,-1):
        if (a[i]+a[j]==tar):
            print(a[i],a[j])
    break
  
