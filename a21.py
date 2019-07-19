from itertools import combinations
Si,s1=map(int,input().split())
li=len(str(Si))
lstc=list(combinations(str(Si),li-s1))
lstc=sorted(lstc)
print(*lstc[0],sep='')
