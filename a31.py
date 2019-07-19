ac2=int(input())
bc2=list(map(int,input().split()))
c1=0
for m in range(0,ac2):
    for p in range(0,m):
        if bc2[p]<bc2[m]:
            c1=c1+bc2[p]
print(c1)
