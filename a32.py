pc1=int(input())
pc2=0
pc3=[]
for j in range(1,pc1+1):
  pc3.append(j)
for j in range(len(pc3)):
  for j in range(j+1,len(pc3)):
    pc2+=1
print(pc2)
