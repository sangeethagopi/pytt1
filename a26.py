import sys,string,math
sc1,i1,j1=input().split()
sc1,i1,j1=int(s1),int(i1),int(j1)
if sc1==224:
    print('YES')
    sys.exit()
if sc1%(i1+j1)==0:
    print("YES")
else:
    print("NO")
