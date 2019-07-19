s1=input()
a1=list(map(int,input().split()))
t=[]
for i in range(len(a1)):
  if i % 2 == 0:
    if a[i] % 2 != 0:
      t.append(a1[i])
  else:
    if a1[i] % 2 == 0:
      t.append(a1[i])
for i in t:
  print(i,end=" ")
      
