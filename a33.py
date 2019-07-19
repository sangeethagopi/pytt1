sc1,t1 = map(int,input().split())
l11 = []
l21 = []
l11 = input().split()
for ic in range(len(l11)):
    l11[ic] = int(l11[ic])
for ic in range(t1):
    a,b = map(int,input().split())
    res = 0
    for ic in range(a-1,b):
        res += l11[ic]
    print(res)
