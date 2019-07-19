import math
pc1,qc1=map(int,input().split())
n1=[]
v1=list(map(int,input().split()))
for i in range(0,qc1):
        a1,b1=map(int,input().split())
        n1.append([a1,b1])
for i in n1:
        x1=i[0]-1
        y1=i[1]-1
        print(math.gcd(v1[x1],v1[y1]))
