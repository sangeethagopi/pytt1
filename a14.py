n1=int(input())
a1=list(map(int,input().split()))
l=len(a1)
for i in range(l):
    for j in range(l):
        for k in range(l):
            if((a1[i]+a1[j]==a1[k]) and (i<j<k)):
                print(a1[i],a1[j],a1[k])
