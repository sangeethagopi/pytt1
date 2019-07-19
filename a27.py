sc1=int(input())
a1=list(map(int,input().split()))
r1=0
for i in range(sc1):
  for j in range(i,sc1):
      for k in range(j,sc1):
          if(a1[i]<a1[j]<a1[k]):
            r1+=1
print(r1)
