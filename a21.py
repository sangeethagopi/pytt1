from itertools import combinations
Si,s1=map(int,input().split())
li=len(str(Si))
lst=list(combinations(str(Si),li-s1))
lst=sorted(lst)
print(*lst[0],sep='')
