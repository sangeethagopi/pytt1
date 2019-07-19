    
np1=int(input())
ap1=list(map(int,input().split()))
t=max(ap1)
c,d=0,0
for i in range(0,len(ap1)-1):
  for j in range(i+1,len(ap1)):
    if abs(ap1[i]+ap1[j])<t:
      c,d=ap1[i],ap1[j]
      t=abs(c+d)
print(c,d)
