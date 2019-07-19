n1,k=map(int,input().split())
ac=list(map(int,input().split()))

b=set(ac)
bb=sorted(b, reverse=False)
#print(bb)
c=list(bb)

print(c[-k])
