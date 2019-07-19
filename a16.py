nc1=list(map(int,input().split()))
ac1=list(map(int,input().split()))
b1=list(map(int,input().split()))
l1=len(ac1)
m1=len(b1)
s1=[]
for i in range(l1):
    for j in range(m1):
        if(ac1[i]==b1[j]):
            s1.append(b1[j])
b1.sort()
s1.sort()
if(s1==b1):
    print("YES")
else:
    print("NO")
