a,b=map(int,input().split())
li1=list(map(int,input().split()))[:a]
li2=list(map(int,input().split()))[:b]
res=[]
for i in range(len(li1)):
        for j in range(len(li2)):
                if(li1[i]==li2[j]):
                        res1.append(li2[j])
res1.sort()
li2.sort()
if(res1==li2):
        print("YES")
else:
        print("NO")
